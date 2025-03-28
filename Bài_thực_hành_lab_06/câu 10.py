import random
# Sử dụng list comprehension để tạo danh sách các số chia hết cho cả 5 và 7 trong khoảng 0-200
so_chia_het = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]

# Chọn ngẫu nhiên một số từ danh sách trên
so_ngau_nhien = random.choice(so_chia_het)

print("Số ngẫu nhiên chia hết cho cả 5 và 7 (0-200):", so_ngau_nhien)