str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

n = len(str1)
m = len(str2)
dp = [[0] * (m + 1) for _ in range(n + 1)]

max_len = 0
vi_tri_ket_thuc = 0  

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                vi_tri_ket_thuc = i
        else:
            dp[i][j] = 0

chuoi_chung_dai_nhat = str1[vi_tri_ket_thuc - max_len : vi_tri_ket_thuc]

print("Chuỗi con chung dài nhất là:", chuoi_chung_dai_nhat)
