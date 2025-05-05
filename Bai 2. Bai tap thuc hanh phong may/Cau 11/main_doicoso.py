from doicoso import doicoso1, doicoso2

print("=== Doi so nguyen sang he khac ===")
n = int(input("Nhap so nguyen: "))
print("Nhi phan:", doicoso1.sang_nhi_phan(n))
print("Bat phan:", doicoso1.sang_bat_phan(n))
print("Thap luc phan:", doicoso1.sang_thap_luc_phan(n))

print("\n=== Xu ly chuoi so he khac ===")
chuoi = input("Nhap chuoi so: ")

chuoi_sach = doicoso2.xoa_ky_tu_khong_hop_le(chuoi)
print("Chuoi hop le:", chuoi_sach)
print("He co so xac dinh:", doicoso2.xac_dinh_he_co_so(chuoi_sach))

if chuoi_sach.isdigit():
    print("Tu co so 2 sang 10:", doicoso2.co_so_2_sang_10(chuoi_sach))
    print("Tu co so 8 sang 10:", doicoso2.co_so_8_sang_10(chuoi_sach))
    print("Tu co so 16 sang 10:", doicoso2.co_so_16_sang_10(chuoi_sach))
