print ("Enter the year : ")
endYear = int(input())
startYear =2020
print ("List of leap years:")
for year in range(startYear, endYear):
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
     print (year)