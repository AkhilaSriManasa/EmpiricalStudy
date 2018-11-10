
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:33:55 2018
@author: Akhila Sri Manasa
"""
from lxml import html
import requests
import os
import csv
all_items = list()
all_links = list()
all_files = list()
data_list = list()
data_listN = list()
data_listFiles = list()
def scrape(url,xpath):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    global all_items 
    tmp = tree.xpath(xpath)
    for ele in tmp:
        all_items.append(ele)
        print(ele)
    print(all_items)
     

def scrapeNew(url,xpath):
    global all_links
    page = requests.get(url)
    tree = html.fromstring(page.content)
     
    tmp = tree.xpath(xpath)
    size_tmp = len(tmp)

    for ele in tmp:
        print(ele.strip())
    all_links = tmp
        

def scrapeNew1(url,xpath):
    global all_files
    all_files = []
    page = requests.get(url)
    tree = html.fromstring(page.content)
     
    tmp = tree.xpath(xpath)
    size_tmp = len(tmp)

    for ele in tmp:
        print(ele.strip()) 
    all_files = tmp
      
def scrapeNew2(url,xpath):
    global all_files1
    page = requests.get(url)
    tree = html.fromstring(page.content)
     
    tmp = tree.xpath(xpath)
    size_tmp = len(tmp)

    for ele in tmp:
        print(ele.strip()) 
    all_files1 = tmp
    
temp_url = "https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value"
#for folder names
scrape(temp_url,"//div[@id='answer-613218']/div/div[2]/div[1]/pre[4]/code/text()")
 #"+str(page_no)+"   //*[@id="answer-613218"]/div/div[2]/div[1]/pre[1]/code

print(all_items[0])

print("DATA INSIDE PAGE")

#for folders inside folder names
for item in all_items:
    new_data = {"PROJECT": item}
    data_list.append(new_data)
with open ('tableCodesQ5.txt','a') as file:
            writer = csv.DictWriter(file, fieldnames = ["PROJECT"])            
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)
               

#for item in all_items:
#    Mysize = len(all_links)
#    new_url = "https://github.com/"+str(item)+"Python"
#    scrapeNew(new_url," //a[@class = 'js-navigation-open']/text()")
#    for links in all_links[Mysize:]:
#          new_data = {"FOLDER": links}
#          data_listN.append(new_data)
#         
#    with open (os.path.join('C:\sqlite\Scrape',('table_'+str(item[0:4])+'.csv')),'w') as file:
#            writer = csv.DictWriter(file, fieldnames = ["FOLDER"])            
#            writer.writeheader()
#            for row in data_listN:
#                writer.writerow(row)
#    del data_listN[:]            
#
#    for link in all_links:
#        tmp_url = "https://github.com/"+str(item)+"/Python/tree/master/"+str(link)+""
#        scrapeNew1(tmp_url," //a[@class = 'js-navigation-open']/text()")
#        for files in all_files:
#           new_data = {"FILES": files}
#           data_listFiles.append(new_data)
#        
#        with open (os.path.join('C:\sqlite\Scrape',('table_'+str(item[0:4])+'_tab_'+str(link[0:4])+'.csv')),'w') as file:
#            writer = csv.DictWriter(file, fieldnames = ["FILES"])            
#            writer.writeheader()
#            for row in data_listFiles:
#                writer.writerow(row)
#        del data_listFiles[:]       
#
#             
#        for file in all_files:
#            if file[-3:] != ".py":
#                continue
#        
#            newer_url = "https://raw.githubusercontent.com/"+str(item)+"Python/master/"+str(link)+"/"+str(file)+""
#            #scrapeNew2(newer_url," //text()")
#            sc = requests.get(newer_url).content
#            f = open(os.path.join('C:\sqlite\Scrape\TwoW\Scripts',file), "wb")
#            f.write(sc)
#            f.close()
