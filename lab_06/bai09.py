n = list(map(int, input("Nhập dãy các số cách nhau bằng dấu cách: ").split()))
a = True  

# Duyệt qua từng phần tử trong danh sách để kiểm tra
for num in n:
    if num % 2 != 0:
        a = False  # Nếu có số lẻ thì gán all_even thành False
        break  # Không cần kiểm tra tiếp vì đã phát hiện số lẻ

# In kết quả
if a:
    print("Tất cả các số trong danh sách đều là số chẵn.")
else:
    print("Danh sách chứa ít nhất một số không phải là số chẵn.")
