import os,sys
import cgi
import cgitb; cgitb.enable()
os.environ[ 'HOME' ] = '/tmp/'


import matplotlib
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='wordpress')
cursor=cnx.cursor()
query="Select qA from wp_kmsurvey_data"
cursor.execute(query)
result=list(cursor.fetchall())
cnx.close()

matplotlib.use( 'Agg' )
import pylab
#pylab.figure(figsize=(7,10))
#Deals with inputing data into python from the html form
form = cgi.FieldStorage()
labels = 'LTE Attach Detach', 'SGSN \n Attach Detach','C-SGN', 'Openstack', 'Basics of Networking','SDN/NFV', 'Python', 'PERL', 'Boot Hardware & \n Instantiate vMME','Upgrade vMME'
sizes = result
colors = ['#5BDFD7', 'lightcoral', '#53CFC7', '#3AB7AF'] 
explode = (0, 0.1, 0, 0,0, 0.1, 0, 0,0, 0.1)    # proportion with which to offset each wedge

pylab.pie(sizes,              # data
        explode=explode,    # offset parameters 
        labels=labels,      # slice labels
        colors=colors,      # array of colours
        autopct='%1.1f%%',  # print the values inside the wedges
        shadow=True,        # enable shadow
        startangle=70,		# starting angle
		wedgeprops={'linewidth':0}
        )
pylab.title('Knowledge Level',y=1.08,fontsize=16,fontweight='bold')
pylab.axis('equal')

#print "Content-Type:text/html\n\n"
#print "Content-type: text/html; charset=utf-8"
# save the plot as a png and output directly to webserver
pylab.savefig( "tempfile1.png", format='png' )
#import shutil
#shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)

data_uri = open('tempfile1.png', 'rb').read().encode('base64').replace('\n', '')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

print(img_tag)


def a():
	return 'test'

def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/html')])	
	a1=a()
	yield a1