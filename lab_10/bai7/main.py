import dayso
ds=dayso.taojdayso(50)
print("Day so duoc tao: ")
print(ds)

ntchia7=dayso.chia_7_nt(ds)
print(f"\n Cac so nt chia het cho 7 la: {ntchia7}")

tong_le=dayso.tong_so_le(ds)
print(f'\n Tong so le: {tong_le}')

if dayso.co_so_chinh_phuong(ds):
    print("Day co chua so chinh phuong")
else:
    print("Day khon gchua so chinh phuong")
    