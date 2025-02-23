so = int(input("Nhập số nguyên có ba chữ số: "))
so_hang_tram = ["", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
so_hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

tram = so // 100
chuc = (so // 10) % 10
don_vi = so % 10

if 100 <= so <= 999:
    print(f"{so_hang_tram[tram]} trăm {so_hang_don_vi[chuc]} mươi {so_hang_don_vi[don_vi]}")
else:
    print("Số không hợp lệ!")
