def Merge(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {'l':6,'g':5}
dict2 = {'d':3,'e':2}
print(Merge(dict1, dict2))
print(dict2)
