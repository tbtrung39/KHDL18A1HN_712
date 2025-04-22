# Cau 4.
def permute(arr, l ,r):
    if l == r :
        print(arr)
    else:
        for i in range (l, r+1):
            arr[l],arr[i],arr[l]
            permute(arr,l+1,r)
            arr[l],arr[i]=arr[i],arr[l]
n=int(input("Nhap so tu nhien n:"))
arr=list(range(1,n+1))
permute(arr,0,n-1)