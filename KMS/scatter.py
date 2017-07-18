import matplotlib
import os,sys
import cgi
import cgitb; cgitb.enable()

matplotlib.use( 'Agg' )
import pylab
import pandas as pd
import mysql.connector
import datetime

month = datetime.datetime.now().strftime("%m")

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='wordpress')
# cursor=cnx.cursor()
# query="Select qA from wp_kmsurvey_data"
# cursor.execute(query)
# result=list(cursor.fetchall())

tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)
ax = pylab.subplot(111)   
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)
title_font = {'fontname':'Arial', 'size':'16', 'color':'black', 'weight':'bold',
              'verticalalignment':'bottom'}
#ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()
pylab.ylim(0, 90)    
#pylab.xlim(1968, 2014)
pylab.yticks(range(0, 91, 10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)    
#pylab.xticks(fontsize=14)
pylab.tick_params(axis="both", which="both", bottom="off", top="off",    
                labelbottom="on", left="off", right="off", labelleft="on")
majors=['LTE Attach Detach', 'SGSN Attach Detach','C-SGN', 'Openstack', 'Basics of Networking','SDN/NFV', 'Python', 'PERL', 'Boot Hardware & Instatiate vMME','Upgrade vMME']
pylab.title('Knowledge Level Comparison', **title_font)
ax.set_ylabel('Percentage(%) of participants')
ax.set_xticklabels(('LTE','SGSN','C-SGN','Open\nstack/\nVM','Network\nBasics','SDN/\nNFV','Python','PERL','Boot\nHardware','Upgrade\nvMME'))
######################################################################################################################################
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=12;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	dec=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=1;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	jan=list(i)
#cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=2;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	feb=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=3;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	mar=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=4;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	apr=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=5;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	may=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=6;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	jun=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=7;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	jul=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=8;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	aug=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=9;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	sep=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=10;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	oct=list(i)
cursor=cnx.cursor()
query="Select q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 from wp_kmsurvey_month_data where month_id=11;"
cursor.execute(query)
result=list(cursor.fetchall())
for i in result:
	nov=list(i)
######################################################################################################################################

if(month=='12'):
	ax.plot(dec,lw=2.5, color=tableau20[12])
	
if(month=='01'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])
	
if(month=='02'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])
if(month=='03'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])
if(month=='04'):  
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])
if(month=='05'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])    
	ax.plot(may,lw=2.5, color=tableau20[5])
if(month=='06'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])    
	ax.plot(may,lw=2.5, color=tableau20[5])   
	ax.plot(jun,lw=2.5, color=tableau20[6])
if(month=='07'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])    
	ax.plot(may,lw=2.5, color=tableau20[5])   
	ax.plot(jun,lw=2.5, color=tableau20[6])    
	ax.plot(jul,lw=2.5, color=tableau20[7])
if(month=='08'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])    
	ax.plot(may,lw=2.5, color=tableau20[5])   
	ax.plot(jun,lw=2.5, color=tableau20[6])    
	ax.plot(jul,lw=2.5, color=tableau20[7])
	ax.plot(aug,lw=2.5, color=tableau20[8])
if(month=='09'): 
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])    
	ax.plot(may,lw=2.5, color=tableau20[5])   
	ax.plot(jun,lw=2.5, color=tableau20[6])    
	ax.plot(jul,lw=2.5, color=tableau20[7])
	ax.plot(aug,lw=2.5, color=tableau20[8])   
	ax.plot(sep,lw=2.5, color=tableau20[9])
if(month=='10'): 
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])    
	ax.plot(may,lw=2.5, color=tableau20[5])   
	ax.plot(jun,lw=2.5, color=tableau20[6])    
	ax.plot(jul,lw=2.5, color=tableau20[7])
	ax.plot(aug,lw=2.5, color=tableau20[8])   
	ax.plot(sep,lw=2.5, color=tableau20[9])   
	ax.plot(oct,lw=2.5, color=tableau20[10])
if(month=='11'):
	ax.plot(dec,lw=2.5,color=tableau20[12])
	ax.plot(jan,lw=2.5, color=tableau20[1])    
	ax.plot(feb,lw=2.5, color=tableau20[2])   
	ax.plot(mar,lw=2.5, color=tableau20[3])	
	ax.plot(apr,lw=2.5, color=tableau20[4])    
	ax.plot(may,lw=2.5, color=tableau20[5])   
	ax.plot(jun,lw=2.5, color=tableau20[6])    
	ax.plot(jul,lw=2.5, color=tableau20[7])
	ax.plot(aug,lw=2.5, color=tableau20[8])   
	ax.plot(sep,lw=2.5, color=tableau20[9])   
	ax.plot(oct,lw=2.5, color=tableau20[10])
    #ax.plot(nov,lw=2.5, color=tableau20[11])
	ax.plot(nov, lw=2.5, color=tableau20[11])

#Deals with inputing data into python from the html form
#pylab.plot([103,34,78,45,23,68,34,2,56,11],lw=2.5,color=tableau20[2])
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
cnx.close()
fontP = FontProperties()
fontP.set_size('xx-small')
dece=mpatches.Patch(color=tableau20[12],label='December')
janu=mpatches.Patch(color=tableau20[1],label='January')
febr=mpatches.Patch(color=tableau20[2],label='Febraury')
marc=mpatches.Patch(color=tableau20[3],label='March')
aprl=mpatches.Patch(color=tableau20[4],label='April')
ma=mpatches.Patch(color=tableau20[5],label='May')
june=mpatches.Patch(color=tableau20[6],label='June')
july=mpatches.Patch(color=tableau20[7],label='July')
augu=mpatches.Patch(color=tableau20[8],label='August')
sept=mpatches.Patch(color=tableau20[9],label='September')
octo=mpatches.Patch(color=tableau20[10],label='October')
nove=mpatches.Patch(color=tableau20[11],label='November')
ax.legend(handles=[dece,janu,febr,marc,aprl,ma,june,july,augu,sept,octo,nove],prop=fontP,frameon=False)
form = cgi.FieldStorage()

# construct your plot
# s = [20*4**n for n in range(4)]
# pylab.plot([1,2,3,4],[1.2,2.2,4.5,7.9])
# #pylab.scatter([1,2,3],[2.2,4.6,9.9],s=s,c='r')
# pylab.xlabel("Testing @ X")
# pylab.text(150, 71, 'India')
# pylab.grid(True)

#print "Content-Type:text/html\n\n"
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