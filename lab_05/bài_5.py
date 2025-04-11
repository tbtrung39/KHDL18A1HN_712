str = input("Nhập chuỗi ký tự : ")
chuoi_so = "".join([ch for ch in str if ch.isdigit()])
print("Chuỗi sau khi lọc chỉ còn số là : ",chuoi_so)
if chuoi_so =="":
    print("Chuỗi không chứa ký tự số nào.")
else:
    num = int(chuoi_so)
    tong_uoc = sum([i for i in range(1, num) if num % i == 0])
    if tong_uoc == num:
        print(num,"là số hoàn hảo")
    else:
        print(num,"không phải là số hoàn hảo")