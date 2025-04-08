# Cau 5.
n=int(input('Nhập vào số n = '))
tong_le=int(0)
tong_chan=int(0)
s=str(n) 
L=len(s)
for i in range(1,L+1):
    if i%2!=0:
        tong_le+= int(s[i-1])
else:
    tong_chan+=int(s[i-1])
print('Tổng các chữ số ở vị trí lẻ của số ',n,'= ',tong_le)
print('Tổng các chữ số ở vị trí chẵn của số ',n,'= ',tong_chan)