chuoi=input('nhap chuoi:')
if not chuoi:
    print('')
else:
    chuoi_con_dai_nhat=''
    chuoi_con_hien_tai=''
    ky_tu_hien_tai=chuoi[0]
    for ky_tu in chuoi:
        if ky_tu==ky_tu_hien_tai:
            chuoi_con_hien_tai+=ky_tu
        else:
            if len(chuoi_con_hien_tai)> len(chuoi_con_dai_nhat):
                chuoi_con_dai_nhat=chuoi_con_hien_tai
                chuoi_con_hien_tai=ky_tu
                ky_tu_hien_tai=ky_tu
    if len(chuoi_con_hien_tai)>len(chuoi_con_dai_nhat):
        chuoi_con_dai_nhat=chuoi_con_hien_tai
    print('chuoi con dai nhat:',chuoi_con_dai_nhat)