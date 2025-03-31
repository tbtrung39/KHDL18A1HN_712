import random
ds = [random.randint(1, 99999) for _ in range(1000)]
ds_sx1 = sorted(ds)
print("10 số đầu (dùng sorted):", ds_sx1[:10])

def sx_chon(a):
    n = len(a)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i] 

ds_sx2 = ds.copy()
sx_chon(ds_sx2)
print("10 số đầu (tự sắp xếp):", ds_sx2[:10])