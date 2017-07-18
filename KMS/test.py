import matplotlib
import os,sys
import cgi
import cgitb; cgitb.enable()

matplotlib.use( 'Agg' )
import pylab

#Deals with inputing data into python from the html form
form = cgi.FieldStorage()

# construct your plot
s = [20*4**n for n in range(4)]
pylab.plot([1,2,3,4],[1.2,2.2,4.5,7.9])
#pylab.scatter([1,2,3],[2.2,4.6,9.9],s=s,c='r')
pylab.xlabel("Testing @ X")
pylab.text(150, 71, 'India')
pylab.grid(True)

print "Content-Type:text/html\n\n"
#print "Content-type: text/html; charset=utf-8"
# save the plot as a png and output directly to webserver
pylab.savefig( "tempfile.png", format='png' )
#import shutil
#shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)

data_uri = open('tempfile.png', 'rb').read().encode('base64').replace('\n', '')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

print(img_tag)

def a():
	return 'test'

def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/html')])	
	a1=a()
	yield a1