""" Update data in the database."""

import connecting as con

def delete_data(eno):
	dele = "UPDATE emptab SET sal = sal+999 WHERE eno = '%d'"

	args = (eno)
	try:
		con.curs.execute(dele % args)
		con.conn.commit()
		print('a row updated')
	except:
		print('Error occured in updating the data..')
		con.conn.rollback()
	finally:
		con.curs.close()
		con.conn.close()

# delete_data(1002)