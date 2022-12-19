import os
import psycopg2

dbname = os.environ['DB']
user = os.environ['USER']
password = os.environ['PASSWORD']
host = os.environ['HOST']

def get_connection():
	return psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

def get_cursor(connection):
	return connection.cursor()

def close_connection(connection):
	connection.close()