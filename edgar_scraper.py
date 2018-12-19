#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
import lxml
from bs4 import BeautifulSoup
cik = input("Enter CIK number")
cik_search_url = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + cik + "&owner=exclude&action=getcompany"

with urllib.request.urlopen(cik_search_url) as response:
   html = str(response.read())
   
soup = BeautifulSoup(html, 'html.parser')

links = []
for x in soup.find_all("tr"):
        if '13F' in x.text:
            links.append(x.a.attrs['href'])
           
        
index = "https://www.sec.gov" + links[0] #first in list is most recent
index_html = urllib.request.urlopen(index).read()
index_soup = BeautifulSoup(index_html, 'html.parser')

full_doc_url = "https://www.sec.gov"
for link in index_soup.find_all('a'):
    if '.txt' in link.text:
        full_doc_url = full_doc_url + link['href']


with urllib.request.urlopen(full_doc_url) as response:
   xml = response.read()
xml_soup = BeautifulSoup(xml)

f = open("myfile.txt", "w")
f.write(xml_soup.get_text())  

f.close()  


# In[ ]:




