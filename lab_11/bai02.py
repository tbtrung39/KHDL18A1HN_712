with open('./lab_11/Inp.txt','r') as f_in:
    noi_dung=f_in.readline().strip()
    cac_so_str=noi_dung.split()
    cac_so=[int(so) for so in cac_so_str]
    cac_so.sort()
    noi_dung_ghi=' '.join(map(str,cac_so))
    with open('./lab_11/out.dat','w') as f_out:
        f_out.write(noi_dung_ghi)
        f_out.close()
    print(f'Da doc tu "Inp.txt",sap xep va ghi vao "out.dat" thanh cong')