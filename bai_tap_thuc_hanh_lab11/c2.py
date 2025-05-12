def giai_bai_2(ten_tep_dau_vao="Bai_2_Thuc_hanh_phong_may/Inp.txt",ten_tep_dau_ra="Bai_2_Thuc_hanh_phong_may/out.dat"):
    with open(ten_tep_dau_vao,'r') as f_in:
        noi_dung=f_in.readline().strip()
        cac_so_str=noi_dung.split()
        cac_so=[int(so) for so in cac_so_str]
        cac_so.sort()
        noi_dung_ghi=" ".join(map(str,cac_so))
        with open(ten_tep_dau_ra,'w') as f_out:
            f_out.write(noi_dung_ghi)
        print(f"Da doc tu'{ten_tep_dau_vao}',sap xep va ghi vao'{ten_tep_dau_ra}' thanh cong")
giai_bai_2()