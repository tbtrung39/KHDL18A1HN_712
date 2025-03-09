def main():
    while True:
        ky_tu = input("Nhập một ký tự: ")
        if len(ky_tu) == 1:
            gia_tri_ascii = ord(ky_tu)
            print(f"Giá trị ASCII của ký tự '{ky_tu}' là: {gia_tri_ascii}")
            break
        else:
            print("Vui lòng chỉ nhập một ký tự!")
main()
