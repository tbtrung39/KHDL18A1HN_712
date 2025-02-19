#Câu 12: 
import math 
a= float(input("Nhập vận tốc ban đầu:")) 
log4_5 = math.log(5)/math.log(4) 
t= a/(4*log4_5) 
T = '%0.2f'%(t) 
print("thời gian ô tô đi được cho đến lúc dừng là:", T,"(giây)")