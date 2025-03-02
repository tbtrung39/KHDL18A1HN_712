
def kiem_tra_so_hoan_hao(x):
    tong_uoc_so = 0  
    for i in range(1, x):
        if x % i == 0:  
            tong_uoc_so += i 
    return tong_uoc_so == x  
n = int(input("Nhập vào số n: "))
print(f"Các số hoàn hảo nhỏ hơn {n} là:")
for i in range(1, n):
    if kiem_tra_so_hoan_hao(i):  
        print(i)  



