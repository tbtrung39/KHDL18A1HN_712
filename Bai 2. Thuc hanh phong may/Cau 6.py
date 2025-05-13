# Cau 6.

def la_username_hop_le(username):
    if ' ' in username:
        return False
    for c in username:
        if not (c.isalnum()):  
            return False
    return True
def nhap_danh_sach_email():
    danh_sach = []
    while True:
        try:
            username = input("Nhap username (nhap 'exit' de dung): ")
            if username.lower() == 'exit':
                break
            if not la_username_hop_le(username):
                raise ValueError("Username khong hop le. Chi duoc dung chu cai va chu so, khong co dau cach.")
            email = username + "@companyname.com"
            danh_sach.append(email)
            print("Email da tao:", email)
        except ValueError as e:
            print("Loi:", e)
    return danh_sach
def chay_bai_6():
    danh_sach_email = nhap_danh_sach_email()
    print("\nDanh sach email da nhap:")
    for email in danh_sach_email:
        print(email)
chay_bai_6()