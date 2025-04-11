str = input("Nhập chuỗi ký tự : ")
n = len(str)
max_len = 0
start_index = 0
for i in range(n):
    for j in range(i,n):
        left = i
        right = j
        doi_xung = True
        while left < right :
            if str[left] != str[right]:
                doi_xung = False
                break
            left +=1
            right -= 1
            if doi_xung and (j - i +1 > max_len):
                max_len = j - i + 1
                start_index = i
print("Chuỗi con đối xứng dài nhất là : ",str[start_index:start_index+max_len])