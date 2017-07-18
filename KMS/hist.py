import matplotlib
import os,sys
import cgi
import cgitb; cgitb.enable()
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='wordpress')
cursor=cnx.cursor()
query="Select qC from wp_kmsurvey_data"
cursor.execute(query)
result=list(cursor.fetchall())

res=[i[0] for i in result]

cnx.close()
matplotlib.use( 'TkAgg' )
import pylab
import numpy as np
#Deals with inputing data into python from the html form
form = cgi.FieldStorage()
import matplotlib.pyplot as plt
import prettyplotlib as ppt
# # construct your plot
# # s = [20*4**n for n in range(4)]
# # axes=pylab.gca()
# # #axes.set_xlim([0,100])
# # pylab.xlabel("Topics")
# # bins=range(0,len(result),1)

# # pylab.ylabel("Number of people interested")
# # pylab.hist(result,bins)
# # #pylab.scatter([1,2,3],[2.2,4.6,9.9],s=s,c='r')
# # pylab.yticks([5,10,15,20,25,30,35,40])
# import plotly
# import plotly.graph_objs as go
# plotly.offline.init_notebook_mode()
# data=[go.Bar(x=['hell', 'hello', 'have', 'not'], y=[4, 3, 2, 1])]
# plotly.offline.plot({
    # "data": [go.Bar(x=['hell', 'hello', 'have', 'not'], y=[4, 3, 2, 1])],
    # "layout": go.Layout(title="hello world")
# },image='png')
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold',
              'verticalalignment':'bottom'}
res=tuple(res)
ind=np.arange(10)
width=0.5
fig, ax=plt.subplots(figsize=(8,8))
rects=ax.bar(ind,res,width,color='#5BDFD7',edgecolor='none')
ax.set_ylabel('Interested Number of People')
ax.set_title('What People Showed Interest In', **title_font)
ax.set_xticks(ind+width)
ax.set_xticklabels(('LTE','SGSN','C-SGN','Open\nstack/\nVM','Network\nBasics','SDN/\nNFV','Python','PERL','Boot\nHardware','Upgrade\nvMME'),rotation=90)
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)
plt.tick_params(axis="both", which="both", bottom="off", top="off",    
                labelbottom="on", left="off", right="off", labelleft="on")
#######################################use when data needed in precentage ############################
# plt.yticks(range(0, 91, 10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)    
# plt.xticks(fontsize=14) 
######################################################################################################
#print "Content-Type:text/html\n\n"
#print "Content-type: text/html; charset=utf-8"
# save the plot as a png and output directly to webserver
pylab.savefig( "tempfile3.png", format='png' )
#import shutil
#shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)

data_uri = open('tempfile3.png', 'rb').read().encode('base64').replace('\n', '')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

print(img_tag)

def a():
	return 'test'

def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/html')])	
	a1=a()
	yield a1