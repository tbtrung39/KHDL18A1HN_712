a = [2, -4, 1, 9 -3, 6, 3, -2, 6, 8]
sum = 0
for i in a:
    sum += i
print('Tổng các phần tử trong damh sách: %d'%sum)
# Dếm số lượng hạng tử dương và tính tổng
số_dương = 0
tổng_dương = 0
for i in a:
    if i > 0:
      số_dương += 1
      tổng_dương += i
print("Số lượng các hạng tử dương là: ",số_dương )
print("Tổng các số hạng dương là: ", tổng_dương)
#vị trí phần tử âm đầu tiên
vị_trí_âm_dầu = None
for i in range(len(a)):
   if a[i] <0:
      vị_trí_âm_dầu = i
      break
print('Vị trí phần tử âm đầu tiên là:', vị_trí_âm_dầu)
# Vị trí phần tử duong cuối 
vị_trí_dương_cuối = None
for i in range(len(a)-1, -1, -1):
   if a[i] >0:
      vị_trí_dương_cuối =i
print('Vị trí phần tử dương cuối là: ', vị_trí_dương_cuối)
# Phần tử lớn nhất danh sách và vị trí phần tử lớn nhất cuối cùng
max_value= max(a)
vị_trí_lớn_nhất_cuối =len(a)-1-a[::-1].index(max_value)
giá_trị_lớn_nhất= max(a)
print('Giá tị lớn nhất danh sách là:', giá_trị_lớn_nhất)
print('Phần tử lớn nhất cuối danh sách là:', vị_trí_lớn_nhất_cuối) 
