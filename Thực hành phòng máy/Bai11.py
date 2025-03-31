import random
danh_sach_A = list(map(int, input("Nhập danh sách A (các số nguyên cách nhau bởi dấu cách): ").split()))
# a. 
danh_sach_B = [so for so in danh_sach_A[:5] if so % 3 == 0 and so % 5 != 0]
print("\nDanh sách B (chia hết cho 3 nhưng không chia hết cho 5, từ 5 phần tử đầu):", danh_sach_B)
# b. 
danh_sach_C = [so ** 2 for so in danh_sach_A]
print("\nDanh sách C (bình phương của danh sách A):", danh_sach_C)
# c. 
danh_sach_chia_het_3 = [so for so in danh_sach_A if so % 3 == 0]
danh_sach_D = random.sample(danh_sach_chia_het_3, min(len(danh_sach_chia_het_3), 3))
print("\nDanh sách D (các phần tử ngẫu nhiên từ A chia hết cho 3):", danh_sach_D)
