n = int(input('Nhap vao so tu nhien n: '))
A = {i for i in range(1, n+1) if n% i == 0}
B = {i for i in range(1, n) if i not in A}
print('Tap hop A la uowc cua n: ', A)
print('Tap hop B la so nho hon n va ko la uoc cua A:', B)
