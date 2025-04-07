h=(161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170)
n=len(h)
#a
print('nhom co so sinh vien la:',n)
#b
tong=0
for i in h:
    tong+=i
print('chieu cao trung binh la %0.2f'%(tong/n))
#c
khac=set(h)
khac_sorted=sorted(list(khac))
print('cac chieu cao khac nhau la:')
for h in khac_sorted:
    print(h)
