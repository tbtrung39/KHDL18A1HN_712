# bai12
balance = 0

while True:

    transaction = input("Nhập giao dịch (D <số tiền> để gửi, W <số tiền> để rút, Enter để kết thúc): ").strip()

    if not transaction:
        break

    try:
        action, amount = transaction.split()
        amount = int(amount)

        if action.upper() == "D":  
            balance += amount
        elif action.upper() == "W": 
            balance -= amount
        else:
            print("Lệnh không hợp lệ, vui lòng nhập lại.")
    except ValueError:
        print("Định dạng không hợp lệ, vui lòng nhập lại.")

print("Số dư tài khoản cuối cùng:", balance)

