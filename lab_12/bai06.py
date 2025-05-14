def kiểm_tra_hợp_lệ(tên_người_dùng):
    return tên_người_dùng.isalpha()

def tạo_email_công_ty():
    danh_sách_email = []
    while True:
        tên_người_dùng = input("Nhập tên người dùng (hoặc 'thoát' để kết thúc): ")
        if tên_người_dùng.lower() == "thoát":
            break
        if not kiểm_tra_hợp_lệ(tên_người_dùng):
            print("Lỗi: Tên người dùng chỉ được chứa chữ cái a-z, A-Z.")
            continue
        địa_chỉ_email = tên_người_dùng + "@companyname.com"
        danh_sách_email.append(địa_chỉ_email)
        print(f"Đã thêm: {địa_chỉ_email}")
    return danh_sách_email

danh_sách = tạo_email_công_ty()
print("Danh sách email đã nhập:")
for email in danh_sách:
    print(email)
