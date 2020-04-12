import urllib.request as ur
import xml.etree.ElementTree as ET
import ssl
#from xml.etree.ElementTree import fromstring, ElementTree

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url)<1 :
    url= "http://py4e-data.dr-chuck.net/comments_42.xml"
print('Retrieving', url)
uh = ur.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data.decode())
sum=0
count=0
counts = tree.findall('.//count')
for i in counts:    
    sum += int(i.text)
    count +=1
print("Count:",count)
print("Sum:",sum)
  