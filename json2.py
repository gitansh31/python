import json
import urllib.request as ur

url = input ("Enter url- ")
print("Retrieving",url)
data = ur.urlopen(url).read()

print("Retrieved", len(data),"characters")
txt = json.loads(data.decode())

info = txt["comments"]
print('User count:', len(info))
sum = 0
for item in info:
    #print('Name', item['name'])
     sum += int(item['count'])
print("Sum:",sum)
