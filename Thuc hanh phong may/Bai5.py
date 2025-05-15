def hoan_vi(lst):
    if len(lst) == 1:
        return [lst]
    
    result = []
    for i in range(len(lst)):
        x = lst[i]
        sublist = lst[:i] + lst[i+1:]
        for p in hoan_vi(sublist):
            result.append([x] + p)
    return result
def permutation(n):
    lst = list(range(1, n + 1))
    return hoan_vi(lst)
n = int(input("Nhập số nguyên n: "))
ket_qua = permutation(n)
print(f"Tất cả các hoán vị của dãy [1..{n}]:")
for p in ket_qua:
    print(p)
