# Câu 2.
# Câu lệnh if-elif-else
# a) Nhập điểm số và xếp loại (Giỏi, Khá, Trung bình, Yếu).
# b) Kiểm tra tuổi nhập vào có hợp lệ để đi bầu cử không.
# c) Kiểm tra nhiệt độ nhập vào có phù hợp để ra ngoài hay không

# a.
diem = float(input("Nhập điểm số: "))
if diem >= 8.5:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

# b.
tuoi = int(input("Nhập tuổi: "))
if tuoi >= 18:
    print("Bạn đủ tuổi để đi bầu cử.")
else:
    print("Bạn chưa đủ tuổi để đi bầu cử.")

# c.
nhiet_do = float(input("Nhập nhiệt độ: "))
if nhiet_do >= 30:
    print("Nhiệt độ quá cao, không nên ra ngoài.")
elif nhiet_do >= 20:
    print("Thời tiết dễ chịu, có thể ra ngoài.")
else:
    print("Nhiệt độ quá thấp, nên ở trong nhà.")
