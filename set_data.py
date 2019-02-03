""" Inserting data into databse table."""
import connecting as con

ins = "INSERT INTO emptab(eno, ename, sal) VALUES(1004, 'kim', 120000)"

try:
	con.curs.execute(ins)
	con.conn.commit()
	print('a row inserted')
except:
	print('Error occured in inserting the data..')
	con.conn.rollback()


# for row in rows:
# 	eno = row[0]
# 	ename = row[1]
# 	sal = row[2]
# 	print('%-6d %-15s %10.2f'% (eno, ename, sal))