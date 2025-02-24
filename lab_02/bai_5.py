def ten_thang(thang):
    thang_ten = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return thang_ten.get(thang, "Tháng không hợp lệ")

while True:
    thang = int(input("Nhập vào tháng (1-12): "))
    if 1 <= thang <= 12:
        break
    print("Tháng nhập vào không hợp lệ, vui lòng nhập lại.")
print(f"Tháng {thang} có tên là {ten_thang(thang)}")
