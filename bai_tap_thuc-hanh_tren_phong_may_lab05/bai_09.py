chuoi=input('nhap chuoi:')
if not chuoi:
    print('')
else:
    chuoi_dai_nhat=''
    chuoi_ngan=''
    ky_tu_hien_tai=chuoi[0]
    for ky_tu in chuoi:
        if ky_tu==ky_tu_hien_tai:
            chuoi_ngan+=ky_tu
        else:
            if len(chuoi_ngan)> len(chuoi_dai_nhat):
                chuoi_dai_nhat=chuoi_ngan
                chuoi_ngan=ky_tu
                ky_tu_hien_tai=ky_tu
    if len(chuoi_ngan)>len(chuoi_dai_nhat):
        chuoi_dai_nhat=chuoi_ngan
    print('chuoi dai nhat:',chuoi_dai_nhat)