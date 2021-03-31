stringA = "I am going home"
print("Given String: \n",stringA)
vowels = "AaEeIiOoUu"
res = set([each for each in stringA if each in vowels])
print("The vowels present in the string:\n ",res)