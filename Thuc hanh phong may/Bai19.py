# a. Tạo mới từ điển
nhan_vien = {}

# Nhập số lượng nhân viên ban đầu
n = int(input("Nhập số lượng nhân viên: "))

# Nhập thông tin ban đầu cho n nhân viên
for _ in range(n):
    while True:
        ma_nv = input("Nhập mã nhân viên (4 ký tự số): ")
        if ma_nv.isdigit() and len(ma_nv) == 4:
            break
        print("Mã nhân viên phải là 4 ký tự số! Vui lòng nhập lại.")
    
    ho_ten = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")[:20]  # Cắt tối đa 20 ký tự
    
    while True:
        try:
            nam_sinh = int(input("Nhập năm sinh: "))
            if 1900 <= nam_sinh <= 2025:  # Giới hạn năm sinh hợp lý
                break
            print("Năm sinh phải từ 1900 đến 2025! Vui lòng nhập lại.")
        except ValueError:
            print("Năm sinh không hợp lệ! Vui lòng nhập lại.")
    
    while True:
        try:
            luong = float(input("Nhập lương: "))
            if luong >= 0:
                break
            print("Lương phải là số không âm! Vui lòng nhập lại.")
        except ValueError:
            print("Lương không hợp lệ! Vui lòng nhập lại.")
    
    nhan_vien[ma_nv] = {'ho_ten': ho_ten, 'nam_sinh': nam_sinh, 'luong': luong}

# b. Thêm nhân viên mới
while True:
    them = input("Thêm nhân viên mới? (y/n): ").lower()
    if them == 'n':
        break
    elif them == 'y':
        while True:
            ma_nv = input("Nhập mã nhân viên (4 ký tự số): ")
            if ma_nv.isdigit() and len(ma_nv) == 4 and ma_nv not in nhan_vien:
                break
            print("Mã nhân viên không hợp lệ hoặc đã tồn tại! Vui lòng nhập lại.")
        
        ho_ten = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")[:20]
        
        while True:
            try:
                nam_sinh = int(input("Nhập năm sinh: "))
                if 1900 <= nam_sinh <= 2025:
                    break
                print("Năm sinh phải từ 1900 đến 2025! Vui lòng nhập lại.")
            except ValueError:
                print("Năm sinh không hợp lệ! Vui lòng nhập lại.")
        
        while True:
            try:
                luong = float(input("Nhập lương: "))
                if luong >= 0:
                    break
                print("Lương phải là số không âm! Vui lòng nhập lại.")
            except ValueError:
                print("Lương không hợp lệ! Vui lòng nhập lại.")
        
        nhan_vien[ma_nv] = {'ho_ten': ho_ten, 'nam_sinh': nam_sinh, 'luong': luong}
        print("Đã thêm nhân viên thành công!")
    else:
        print("Vui lòng nhập 'y' hoặc 'n'!")

# c. Tìm kiếm nhân viên
x = input("Nhập mã nhân viên để tìm kiếm (x): ")
if x in nhan_vien:
    info = nhan_vien[x]
    print(f"Mã: {x}, Họ tên: {info['ho_ten']}, Năm sinh: {info['nam_sinh']}, Lương: {info['luong']}")
else:
    print("Không tìm thấy nhân viên với mã này.")

# d. Tăng lương
y = input("Nhập mã nhân viên để tăng lương (y): ")
if y in nhan_vien:
    nhan_vien[y]['luong'] += 1000000
    print(f"Đã tăng lương cho nhân viên {y}. Lương mới: {nhan_vien[y]['luong']}")
else:
    print("Không tìm thấy nhân viên với mã này.")

# e. Xóa nhân viên
z = input("Nhập mã nhân viên để xóa (z): ")
if z in nhan_vien:
    del nhan_vien[z]
    print(f"Đã xóa nhân viên có mã {z}.")
else:
    print("Không tìm thấy nhân viên với mã này.")

# f. Sắp xếp giảm dần theo năm sinh
sorted_nv = dict(sorted(nhan_vien.items(), key=lambda x: x[1]['nam_sinh'], reverse=True))
print("\nDanh sách nhân viên sau khi sắp xếp giảm dần theo năm sinh:")
for ma_nv, info in sorted_nv.items():
    print(f"Mã: {ma_nv}, Họ tên: {info['ho_ten']}, Năm sinh: {info['nam_sinh']}, Lương: {info['luong']}")