def la_username_hop_le(username):
    return username.isalnum()
def nhap_email_nhan_vien():
    danh_sach_email = []
    while True:
        try:
            username = input("Nhap username (hoac enter de dung): ").strip()
            if username == "":
                break
            if not la_username_hop_le(username):
                raise ValueError("Loi")
            email = username+"@companyname.com"
            danh_sach_email.append(email)
            print("da them: ",email)
        except ValueError as e:
            print(e)
    print("\ndanh sach email nhan vien")
    for email in danh_sach_email:
        print(email)
nhap_email_nhan_vien()