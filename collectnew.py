# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import requests
import pymysql

#============================================================================



r=requests.get('https://www.jin10.com')
r.encoding='utf-8'
#print(r.text)
line=r.text
m=re.findall(r'(flashData)(.*)(var\sadsData)',line)
x=[]
text_list=[]

for i in m[0]: 
    x.append(i)  
    
line_2=x[1]
#year=re.findall(r'\d{4}-\d{2}-\d{2}',line_2)
#time=re.findall(r'\d{2}:\d{2}:\d{2}',line_2)
text=re.findall(r'(\d{2}:\d{2}:\d{2})(.*?)(##)',line_2)
id_1=re.findall(r'\d{20}',line_2)

datetime_list=[]
#time_list=[]
for i in id_1:
    datetime_list.append(i[0:14])
#    time_list.append(i[8:14])

#hi=text[0][1]        
for i in text: 
    temp=i[1] 
    text_list.append(temp) 


#table=list(zip(year,time,text_list,id_1))

#print(table)

 

db = pymysql.connect("192.168.199.121","emi","moyna123","test1" )

cursor = db.cursor()
 
#insertsql = """INSERT IGNORE INTO newstest(id,year_list, time_list, news) VALUES(11111111111,2018-03-04,080923,'wodetian')"""

#try:
for i,j,k in zip(id_1,datetime_list,text_list):
    cursor.execute("INSERT IGNORE INTO newstest(id,datetime_list, news) VALUES(%s,%s,%s)",(i,j,k))

db.commit()
#except:
#   db.rollback()
 
db.close()




'''
with open('E:/text/example.csv', 'w', newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in table:
        writer.writerow(row)



with open('E:/text/text5.html','wb',)as f:
    f.write(r.content)
    


with open('E:/text/text5.txt','w',encoding='utf-8')as f:
    f.write(x[1])
    
'''