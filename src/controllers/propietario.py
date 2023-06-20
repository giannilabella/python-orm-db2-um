from src.database import psycopg2_connect


def listar_propietarios():
    try:
        connection = psycopg2_connect()
    except Exception as e:
        print('Error al conectarse con la base de datos')
        print(e)
        input('Presione enter para continuar...')
        return

    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    select
                        persona_dni,
                        empresa_rut,
                        string_agg(vehiculo_matricula, ', ') as vehiculos
                    from
                        propietario
                    left outer join persona on
                        (propietario_persona_id = persona_id)
                    left outer join empresa on
                        (propietario_empresa_id = empresa_id)
                    left outer join propietariovehiculo on
                        (propietario_id = propietario_vehiculo_propietario_id)
                    left outer join vehiculo on
                        (propietario_vehiculo_vehiculo_id = vehiculo_id)
                    group by
                        persona_dni, empresa_rut;
                """)
            except Exception as e:
                print('Error al listar propietarios')
                print(e)
                input('Presione enter para continuar...')
                return

            for (dni, rut, vehiculos) in cursor.fetchall():
                if dni is None:
                    print(f'Empresa de RUT {rut} es propietaria de los vehiculos de matricula: {vehiculos}')
                else:
                    print(f'Persona de DNI {dni} es propietaria de los vehiculos de matricula: {vehiculos}')
            input('Presione enter para continuar...')

    connection.close()
