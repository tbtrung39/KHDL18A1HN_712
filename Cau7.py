# Câu 7.
# Câu lệnh if-elif-else
# a)	Nhập điểm của một sinh viên và xếp loại theo tiêu chí (Giỏi, Khá, Trung bình, Yếu).
# b)	Nhập nhiệt độ và kiểm tra xem có cần mặc áo ấm không (dựa trên ngưỡng nhiệt độ nhất định).

# a.
diem = float(input("Nhập điểm của sinh viên: "))
if diem >= 8.5:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

# b.
nhiet_do = float(input("Nhập nhiệt độ: "))
if nhiet_do < 20:
    print("Cần mặc áo ấm.")
else:
    print("Không cần mặc áo ấm.")
