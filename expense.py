import sqlite3 as db

def init():

	conn=db.connect("spent.db")
	cur=conn.cursor()
	sql='''
	create table if not exists expenditure(
     amount number,
     category string,
     message string,
     date string
	)
	'''
	cur.execute(sql)
	conn.commit()


def log(amount, category, message=""):
	'''logs the expenditure
	into the database'''
	'''message:optional'''
	from datetime import datetime
	date=str(datetime.now())
	conn=db.connect("spent.db")
	cur=conn.cursor()
	sql='''
	insert into expenditure values(
    {},
    '{}',
    '{}',
    '{}'
	)
	
	'''.format(amount,category,message,date)
	cur.execute(sql)
	conn.commit()

def view(category=None):
	conn = db.connect("spent.db")
	cur = conn.cursor()
	if category:
		sql = '''select * from expenditure where category='{}' '''.format(category)
		sql2 = '''select sum(amount) from expenditure where category='{}' '''.format(category)
	else:
		sql = '''select * from expenditure'''.format(category)
		sql2 = '''select sum(amount) from expenditure '''.format(category)


	cur.execute(sql)

	results = cur.fetchall()
	cur.execute(sql2)
	total_amount = cur.fetchone()[0]
	return total_amount, results



# print(view('food'))


# print(view())


