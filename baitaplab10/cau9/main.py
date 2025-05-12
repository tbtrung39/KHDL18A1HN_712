import quanlyhanghoa
ds=[]
n=int(input("so hang hoa:"))
for _ in range(n):
    ds.append(quanlyhanghoa.nhap_hang())
for h in ds:
    print(f"{h['ten']}:tien={quanlyhanghoa.tinh_tien(h)},thue={quanlyhanghoa.tinh_thue(h)}")
print("sap xep theo thue giam dan:")
ds=quanlyhanghoa.sap_xep(ds)
for h in ds:
    print(f"{h['ten']}:tien={quanlyhanghoa.tinh_tien(h)}")