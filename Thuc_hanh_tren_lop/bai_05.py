months = {1: "January", 2: "February", 3: "March", 4: "April", 
          5: "May", 6: "June", 7: "July", 8: "August", 
          9: "September", 10: "October", 11: "November", 12: "December"}

while True:
    month = int(input("Nhập tháng (1-12): "))
    if 1 <= month <= 12:
        print(f"Tháng {month} là {months[month]}")
        break
    print("Tháng không hợp lệ, vui lòng nhập lại!")