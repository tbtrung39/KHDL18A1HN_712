import qlyhanghoa
ds=[]
n=int(input("so hang hoa:"))
for _ in range(n):
    ds.append(qlyhanghoa.nhap_hang())
for h in ds:
    print(f"{h['ten']}:tien={qlyhanghoa.tinh_tien(h)},thue={qlyhanghoa.tinh_thue(h)}")
print("sap xep theo thue giam dan:")
ds=qlyhanghoa.sap_xep(ds)
for h in ds:
    print(f"{h['ten']}:tien={qlyhanghoa.tinh_tien(h)}")