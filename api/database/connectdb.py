# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:32 2023

@author: Mario
"""

import pyodbc
import psycopg2 as conn2
from decouple import config


def connect_postgresql(hostname, dbname, username, password, port):
    try:
        conn_post = conn2.connect(
        dbname=dbname,
        user=username,
        password=password,
        host=hostname,
        port=port)
        return conn_post
    except Exception as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
        raise Exception(e)


def get_connection():
    try:
        connection = connect_postgresql(
            config('HOSTNAME_PSQL_AWS'),
            config('DATABASE_PSQL_AWS'),
            config('USERNAME_PSQL_AWS'),
            config('PASSWORD_PSQL_AWS'),
            config('PORT_POSTGRES')
        )
        return connection
    except Exception as ex:
        raise Exception(ex)

print(get_connection())

