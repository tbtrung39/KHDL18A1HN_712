n = int(input("Nhập vào một số nguyên: "))

hang_tram = (abs(n) // 100) % 10
#abs để trả về giá trị tuyệt đối
print(f"Chữ số hàng trăm là: {hang_tram}")
