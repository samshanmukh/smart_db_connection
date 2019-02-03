""" Delete data from the database."""

import connecting as con

def delete_data(eno):
	dele = "DELETE FROM emptab WHERE eno = '%d'"

	args = (eno)
	try:
		con.curs.execute(dele % args)
		con.conn.commit()
		print('a row deleted')
	except:
		print('Error occured in deleting the data..')
		con.conn.rollback()
	finally:
		con.curs.close()
		con.conn.close()

# delete_data(1004)