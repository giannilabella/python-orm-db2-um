from sshtunnel import SSHTunnelForwarder
from configparser import ConfigParser
from peewee import PostgresqlDatabase, Model

config = ConfigParser()
config.read('database.cfg')
globalcfg = config['global']
sshtunnelcfg = config['ssh_tunnel']
databasecfg = config['database']

sshtunnel = SSHTunnelForwarder(
    ssh_address_or_host=sshtunnelcfg.get('ssh_host'),
    ssh_port=sshtunnelcfg.getint('ssh_port'),
    ssh_username=sshtunnelcfg.get('ssh_username'),
    ssh_password=sshtunnelcfg.get('ssh_password'),
    remote_bind_address=(
        sshtunnelcfg.get('remote_address'),
        sshtunnelcfg.getint('remote_port')
    ),
    local_bind_address=(
        sshtunnelcfg.get('local_address'),
        sshtunnelcfg.getint('local_port')
    )
)

postgres_db = PostgresqlDatabase(
    databasecfg.get('db_name'),
    host=databasecfg.get('db_host'),
    port=databasecfg.getint('db_port'),
    user=databasecfg.get('db_user'),
    password=databasecfg.get('db_password'),
)


def db_connect():
    if globalcfg.getboolean('use_ssh_tunnel'):
        print('INFO: Opening ssh tunnel...')
        sshtunnel.start()
        if not sshtunnel.is_active:
            print('ERROR: Cannot establish ssh tunnel!')
            return False

    print('INFO: Connecting to database...')
    postgres_db.connect()
    return True


class BaseModel (Model):
    class Meta:
        database = postgres_db
