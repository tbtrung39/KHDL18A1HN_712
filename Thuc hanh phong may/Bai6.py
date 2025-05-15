import random
def random_permutation(n):
    lst = list(range(1, n + 1))
    random.shuffle(lst)
    return lst
n = int(input("Nhập số nguyên n: "))
ket_qua = random_permutation(n)

print(f"Hoán vị ngẫu nhiên của dãy [1..{n}]:")
print(ket_qua)
