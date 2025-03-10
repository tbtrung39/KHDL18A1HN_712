so_thap_phan = input("Nhập vào một số thập phân: ")
chu_so = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
ket_qua = []

for ky_tu in so_thap_phan:
    if ky_tu.isdigit():  
        ket_qua.append(chu_so[int(ky_tu)])
for i in range(len(ket_qua)):
    if i < len(ket_qua) - 1:
        print(ket_qua[i], end=" ")
    else:
        print(ket_qua[i])
