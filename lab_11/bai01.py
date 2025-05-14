with open('./lab_11/dayso.dat','r') as f:
    for line in f:
        cac_so_str=line.strip().split()
        cac_so=[int(so) for so in cac_so_str]
        tong=sum(cac_so)
print(f"Dong: {line.strip()}, tong: {tong}")