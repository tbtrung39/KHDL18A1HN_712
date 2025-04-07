list1 = ['An', 'Bình', 'Châu', 'Duy']
list2 = ['a', 'b', 'c', 'd']

dictionary = {abbr: name for abbr, name in zip(list2, list1)}

print("Từ điển:")
for k, v in dictionary.items():
    print(f"{k}: {v}")
