list1 = [1, 2, 3, 4, 5] 
list2 = ['A', 'B', 'C', 'D', 'E']  
dictionary = {}
for i in range(len(list1)):
    dictionary[list1[i]] = list2[i]
print(dictionary)