import random

def random_permutation(n):
    A = list(range(1, n + 1))
    result = []

    while A:
        idx = random.randint(0, len(A) - 1)  # Chọn ngẫu nhiên 1 chỉ số
        result.append(A[idx])                # Thêm phần tử vào result
        A.pop(idx)                           # Xóa phần tử khỏi A

    return result

n = int(input("Nhập số tự nhiên n: "))
result = random_permutation(n)
print("Hoán vị ngẫu nhiên:", result)
