
Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")
m, n = len(Str1), len(Str2)
dp = [[0] * (n + 1) for _ in range(m + 1)]
max_length = 0
end_pos = 0  
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if Str1[i - 1] == Str2[j - 1]:  
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:  
                max_length = dp[i][j]
                end_pos = i  
longest_common_substring = Str1[end_pos - max_length:end_pos]

print("Chuỗi con chung dài nhất:", longest_common_substring)
