def nhap_nhan_vien():
    return {
        "ten": input("Tên: "),
        "tuoi": int(input("Tuổi: ")),
        "nam_ct": int(input("Năm công tác: "))
    }

def tinh_luong_nv(nv):
    return nv["nam_ct"] * 12000000

def xuat_nv(nv):
    print(f"{nv['ten']}, Tuổi: {nv['tuoi']}, Năm công tác: {nv['nam_ct']}, Lương: {tinh_luong_nv(nv)}")

nv = nhap_nhan_vien()
xuat_nv(nv)