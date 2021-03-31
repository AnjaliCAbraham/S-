a=['anjali','reenu','gretta','aamy']
str1=(' '.join(a))
count=0
for i in str1: 
   if i == 'a': 
      count = count + 1
print("Count of a in the list is : " + str(count))