str = input("Nhập chuỗi ký tự : ")
so_str = ""
for c in str:
    if c >= "0" and c <= "9":
        so_str +=c
if so_str =="":
    print("KHông có ký tự nào là số.")
else:
    print("Chuỗi số sau khi lọc là : ",so_str)
    n= int(so_str)
    tong_uoc = 0
    for i in range(1,n):
        if n % i == 0:
            tong_uoc += i
    if tong_uoc == n:
        print(n,"là số hoàn hảo.")
    else:
        print(n,'không phải là số hoàn hảo.')