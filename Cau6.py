# Câu 6.
# Kiểm tra số đảo ngược
# a)	Nhập một số nguyên và hiển thị số đảo ngược của nó.
# b)	Kiểm tra xem số nhập vào có phải là số đối xứng không.

# a.
so = int(input("Nhập một số nguyên: "))
dao_nguoc = 0
while so != 0:
    dao_nguoc = dao_nguoc * 10 + so % 10
    so //= 10
print("Số đảo ngược là:", dao_nguoc)

# b.
so = int(input("Nhập một số nguyên: "))
so_goc = so
dao_nguoc = 0
while so != 0:
    dao_nguoc = dao_nguoc * 10 + so % 10
    so //= 10
if so_goc == dao_nguoc:
    print(f"{so_goc} là số đối xứng.")
else:
    print(f"{so_goc} KHÔNG phải là số đối xứng.")
