from math import log
a = int(input('Vận tốc ô tô đang chạy: '))
t = a / (4*log(5)/log(4))
print('Thời gian ô tô đi được cho đến lúc dừng là:', round(t, 2),'giây')