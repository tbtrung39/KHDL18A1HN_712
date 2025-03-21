Str = input("Nhập chuỗi ký tự: ")
# Lọc các ký tự số
chuoi_so = ''.join(filter(str.isdigit, Str))
so = int(chuoi_so) if chuoi_so else 0

# Kiểm tra số hoàn hảo
if so >= 2:
    uoc_so = [1]
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            uoc_so.extend([i, so // i])
    la_so_hoan_hao = sum(uoc_so) == so
else:
    la_so_hoan_hao = False

print(f"Chuỗi số sau khi lọc: {chuoi_so}")
print(f"Số {so} {'là' if la_so_hoan_hao else 'không phải là'} số hoàn hảo.")

