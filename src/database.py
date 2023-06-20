from sshtunnel import SSHTunnelForwarder
from configparser import ConfigParser
from peewee import PostgresqlDatabase
from pymongo import MongoClient
import psycopg2

config = ConfigParser()
config.read('database.cfg')
global_config = config['global']

postgres_ssh_tunnel_config = config['postgres_ssh_tunnel']
postgres_database_config = config['postgres']

mongodb_ssh_tunnel_config = config['mongodb_ssh_tunnel']
mongodb_database_config = config['mongodb']

postgres_ssh_tunnel = None
postgres_database = PostgresqlDatabase(
    postgres_database_config.get('db_name'),
    host=postgres_database_config.get('db_host'),
    port=postgres_database_config.getint('db_port'),
    user=postgres_database_config.get('db_user'),
    password=postgres_database_config.get('db_password'),
)
mongodb_ssh_tunnel = None
mongodb_database = MongoClient(None)


def open_ssh_tunnel(ssh_tunnel_config):
    ssh_tunnel = SSHTunnelForwarder(
        ssh_address_or_host=ssh_tunnel_config.get('ssh_host'),
        ssh_port=ssh_tunnel_config.getint('ssh_port'),
        ssh_username=ssh_tunnel_config.get('ssh_username'),
        ssh_password=ssh_tunnel_config.get('ssh_password'),
        remote_bind_address=(
            ssh_tunnel_config.get('remote_address'),
            ssh_tunnel_config.getint('remote_port')
        ),
        local_bind_address=(
            ssh_tunnel_config.get('local_address'),
            ssh_tunnel_config.getint('local_port')
        )
    )
    ssh_tunnel.start()
    if not ssh_tunnel.is_active:
        raise Exception('Could not start SSH tunnel')
    return ssh_tunnel


def psycopg2_connect():
    global postgres_ssh_tunnel
    print('Connecting to database with psycopg2...')

    try:
        if global_config.getboolean('use_ssh_tunnel') and postgres_ssh_tunnel is None:
            postgres_ssh_tunnel = open_ssh_tunnel(postgres_ssh_tunnel_config)
        connection = psycopg2.connect(
            dbname=postgres_database_config.get('db_name'),
            host=postgres_database_config.get('db_host'),
            port=postgres_database_config.getint('db_port'),
            user=postgres_database_config.get('db_user'),
            password=postgres_database_config.get('db_password'),
        )
        print('Connected!')
        return connection
    except Exception:
        if postgres_ssh_tunnel:
            postgres_ssh_tunnel.close()

        raise


def postgres_connect() -> PostgresqlDatabase:
    global postgres_ssh_tunnel
    global postgres_database
    print('Connecting to database with peewee...')

    try:
        if global_config.getboolean('use_ssh_tunnel') and postgres_ssh_tunnel is None:
            postgres_ssh_tunnel = open_ssh_tunnel(postgres_ssh_tunnel_config)
        if postgres_database.is_closed():
            postgres_database.connect()
        print('Connected!')
        return postgres_database
    except Exception:
        if postgres_ssh_tunnel:
            postgres_ssh_tunnel.close()

        if postgres_database:
            postgres_database.close()

        raise


def mongodb_connect() -> MongoClient:
    global mongodb_ssh_tunnel
    global mongodb_database
    print('Connecting to database with pymongo...')

    try:
        if global_config.getboolean('use_ssh_tunnel') and mongodb_ssh_tunnel is None:
            mongodb_ssh_tunnel = open_ssh_tunnel(mongodb_ssh_tunnel_config)
        mongodb_database = MongoClient(
            authSource=mongodb_database_config.get('db_name'),
            host=mongodb_database_config.get('db_host'),
            port=mongodb_database_config.getint('db_port'),
            username=mongodb_database_config.get('db_user'),
            password=mongodb_database_config.get('db_password'),
            authMechanism='DEFAULT',
        ).dbd2g10
        print('Connected!')
        return mongodb_database
    except Exception:
        if mongodb_ssh_tunnel:
            mongodb_ssh_tunnel.close()

        if mongodb_database:
            mongodb_database.close()

        raise
