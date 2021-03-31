list = [10,13,26,29,38,50]
print(list)
for i  in list:
  if(i%2 == 0):
    list.remove(i)
print("list after removing even numbers:")
print(list)