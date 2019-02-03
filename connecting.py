""" Mysql database connection code."""

# Module import
import mysql.connector;

# Connecting with database
conn = mysql.connector.connect(host='localhost', user='root', password='root', database='world')

# Connection testing
if conn.is_connected():
	print('Database connection established...')

curs = conn.cursor()

# cursor.close()
# conn.close()