import re
file = open("regex_sum_418596.txt","r")
string = re.findall("[0-9]+",file.read())
sum =0
count =0
for i in string :
    count +=1
    sum += int(i)
print("there are %d values and sum is %s" %(count,sum))