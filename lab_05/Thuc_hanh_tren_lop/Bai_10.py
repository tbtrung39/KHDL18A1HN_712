a=input("Nhap chuoi 1: ")
b= input("Nhap chuoi 2: ")
n,m=len(a),len(b)
dp = [[0]*(m-1) for _ in range(n+1)]
max_len=0
end=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
            if dp[i][j] > max_len:
                max_len=dp[i][j]
                end=i
s=a[end - max_len:end]
print("Chuoi con chung dai nhat: ",s)