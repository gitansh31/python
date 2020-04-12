# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
 
url = input('Enter URL: ')
count = input("Enter count: ")
position = input("Enter position: ")
for i in range(1,int(count)+1):
    html = urllib.request.urlopen(url, context = ctx ).read()
    soup = BeautifulSoup(html,"html.parser")
# Retrieve all of the anchor tags
    tags = soup('a')
    cnt=0
    for tag in tags:

        #print (tag.get('href', None))
        cnt = cnt + 1
        if (cnt==int(position)):
            url = tag.get('href', None)            
            print (i ,"Retrieving :",url)
            break
print (tag.text)

