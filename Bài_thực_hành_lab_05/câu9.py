chuoi = input("Nhập chuỗi ký tự: ")

chuoi_max = ""
chuoi_hientai = chuoi[0] if chuoi else ""

for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:
        chuoi_hientai += chuoi[i]
    else:
        if len(chuoi_hientai) > len(chuoi_max):
            chuoi_max = chuoi_hientai
        chuoi_hientai = chuoi[i]

if len(chuoi_hientai) > len(chuoi_max):
    chuoi_max = chuoi_hientai

print("Chuỗi con cực đại:", chuoi_max)
