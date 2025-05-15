danh_sach_so = {i: str(bin(i))[2:] for i in range(1, 101)}

print("Tu dien so va nhi phan:")
for so, nhi_phan in danh_sach_so.items():
    print(f"{so}: {nhi_phan}")