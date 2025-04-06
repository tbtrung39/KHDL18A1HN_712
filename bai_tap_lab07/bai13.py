chuoi = input("Nhập chuỗi ký tự: ")
dict_kt = {chuoi[i:i+2]: chuoi.count(chuoi[i:i+2]) for i in range(len(chuoi)-1)}
print("Từ điển 2 ký tự và số lần xuất hiện:", dict_kt)
