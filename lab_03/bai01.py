n = int(input("Nhập giá trị n: "))
ket_qua = 1  
for i in range(1, n + 1):
    ket_qua *= (2 * i + 1) / (2 * i + 3)  
print("Kết quả:", round(ket_qua, 3))  