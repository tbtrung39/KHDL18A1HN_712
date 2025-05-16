def kiem_tra_chuoi(chuoi):
    if not all(c.isalpha() for c in chuoi):
        raise Exception("Lỗi ký tự !!! Chuỗi chỉ được chứa a-z hoặc A-Z.")
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i + 1]:
            raise Exception("Lỗi nhập liệu !!! Có 2 ký tự liên tiếp giống nhau.")
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i + 1] == chuoi[i + 2] == chuoi[i + 3]:
            raise Exception("Lỗi nhập lặp lại !!! Có 4 ký tự liên tiếp giống nhau.")
    for i in range(len(chuoi) - 9):
        if chuoi[i:i + 5] == chuoi[i + 5:i + 10]:
            raise Exception("Lỗi nhập trùng lặp !!! Có chuỗi 5 ký tự giống nhau liên tiếp.")
def main():
    while True:
        try:
            chuoi = input("Nhập chuỗi ký tự: ")
            kiem_tra_chuoi(chuoi)
            print("Chuỗi hợp lệ ✅")
            break
        except Exception as e:
            print(e)
            print("Vui lòng nhập lại!\n")

if __name__ == "__main__":
    main()
