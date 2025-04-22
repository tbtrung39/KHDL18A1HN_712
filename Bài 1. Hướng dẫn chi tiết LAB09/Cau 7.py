# Cau 7.
def count_characters_recursive(string, count):
    if not string:
        return count
    if string[0].isalpha():
        count['alphabet'] += 1
    elif string[0].isdigit():
        count['digit'] += 1
    else:
        count['special'] += 1
    return count_characters_recursive(string[1:], count)
string = input("Nhap mot chuoi ky tu: ")
count = {'alphabet':0, 'digit':0, 'special':0}
count = count_characters_recursive(string, count)
print("So luong cac ky tu chu cai: ", count['alphabet'])
print("So luong ca ky tu chu so: ", count['digit'])
print("So luong cc ky tu dac biet: ", count['special'])