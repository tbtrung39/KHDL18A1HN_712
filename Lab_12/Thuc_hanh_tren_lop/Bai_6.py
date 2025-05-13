def kiemtra_username(u):
    if not u.isalnum():
        raise Exception("Ten khong hop le.")

danh_sach_email = []

try:
    ten = input("Nhap username: ")
    kiemtra_username(ten)

    email = ten + "@companyname.com"
    danh_sach_email.append(email)

    print("Email hop le da tao:", email)

except Exception as e:
    print("Loi:", e)
