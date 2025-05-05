from qlyhanghoa import MatHang

def nhap_danh_sach():
    danh_sach = []
    n = int(input("Nhap so luong mat hang: "))
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        ma = input("Ma hang: ")
        ten = input("Ten hang: ")
        dvt = input("Don vi tinh: ")
        gia = float(input("Don gia: "))
        sl = int(input("So luong: "))
        mh = MatHang(ma, ten, dvt, gia, sl)
        danh_sach.append(mh)
    return danh_sach

def in_danh_sach(ds):
    print(f"\n{'Ma hang':10} {'Ten hang':15} {'Don vi':10} {'Don gia':10} {'So luong':10} {'Thanh tien':12} {'Thue':10}")
    for mh in ds:
        print(mh)

def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda x: x.thue, reverse=True)

# Chuong trinh chinh
ds = nhap_danh_sach()

print("\n--- Danh sach truoc khi sap xep ---")
in_danh_sach(ds)

ds_sap_xep = sap_xep_theo_thue(ds)
print("\n--- Danh sach sau khi sap xep giam dan theo thue ---")
in_danh_sach(ds_sap_xep)
