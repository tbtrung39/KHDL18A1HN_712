def hien_thi_menu():
    print("Menu đồ uống:")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
def main():
    while True:
        hien_thi_menu() 
        try:

            lua_chon = int(input("Chọn đồ uống (1-5): "))
            if lua_chon == 1:
                print("Bạn đã chọn Cafe.")
            elif lua_chon == 2:
                print("Bạn đã chọn Cam vắt.")
            elif lua_chon == 3:
                print("Bạn đã chọn Nước ép cà rốt.")
            elif lua_chon == 4:
                print("Bạn đã chọn Nước lọc.")
            elif lua_chon == 5:
                print("Bạn đã chọn Nước dừa.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
                continue
            tiep_tuc = input("Bạn có muốn gọi đồ uống khác không? (có / không): ").strip().lower()
            if tiep_tuc == "không":
                print("Cảm ơn bạn đã sử dụng dịch vụ!")
                break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ từ 1 đến 5.")
            
main()