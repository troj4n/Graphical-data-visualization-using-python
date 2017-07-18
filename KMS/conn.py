import mysql.connector


def conn():
	
	cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='wordpress')
	cursor=cnx.cursor()
	query="Select qA from wp_kmsurvey_data"
	cursor.execute(query)
	result=list(cursor.fetchall())
	cnx.close()
	return [result]

def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/html')])	
	
	yield conn()