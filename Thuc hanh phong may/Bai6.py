import re

def kiem_tra_username(username):
    # Regex kiểm tra username chỉ chứa chữ cái và số
    if not re.match("^[a-zA-Z0-9]+$", username):
        raise ValueError("Username không hợp lệ! Chỉ được chứa chữ cái và số, không có dấu cách hay ký tự đặc biệt.")
    return True

def main():
    danh_sach_email = []
    
    while True:
        try:
            username = input("Nhập username (hoặc nhập 'exit' để kết thúc): ")
            if username.lower() == "exit":
                break
            
            kiem_tra_username(username)
            email = username + "@companyname.com"
            danh_sach_email.append(email)
            print(f"Email đã tạo: {email}")
        
        except ValueError as ve:
            print(f"Lỗi: {ve}")
    
    print("\nDanh sách email đã nhập:")
    for email in danh_sach_email:
        print(email)

if __name__ == "__main__":
    main()
