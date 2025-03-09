def tinh_tong_chu_so(n):
    tong = 0
    while n > 0:
        tong += n % 10 
        n //= 10  
    return tong
def main():
    while True:
        try:
            so = int(input("Nhập một số nguyên: "))
            ket_qua = tinh_tong_chu_so(abs(so))  
            
            print(f"Tổng các chữ số của số {so} là: {ket_qua}")
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
main()
