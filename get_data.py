"""Fetching data from databse table."""
import connecting as con

con.curs.execute("SELECT * FROM emptab")

# row = con.cursor.fetchone()

# while row is not None:
# 	print(row)
# 	row = con.cursor.fetchone()

rows = con.curs.fetchall()

# for row in rows:
# 	eno = row[0]
# 	ename = row[1]
# 	sal = row[2]
# 	print('%-6d %-15s %10.2f'% (eno, ename, sal))