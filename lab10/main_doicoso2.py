import doicoso2

s = input("Nhập chuỗi ký tự biểu diễn số: ")

print("Biểu diễn trong các hệ:")
try:
    b2, b8, b16 = doicoso2.bieu_dien_he_co_so(s)
    print("Hệ 2:", b2)
    print("Hệ 8:", b8)
    print("Hệ 16:", b16)
except:
    print("Không thể chuyển đổi.")

print("Chuyển từng hệ sang hệ 10:")
print("Từ nhị phân sang 10:", doicoso2.doi_2_sang_10(s))
print("Từ hệ 8 sang 10:", doicoso2.doi_8_sang_10(s))
print("Từ hệ 16 sang 10:", doicoso2.doi_16_sang_10(s))
