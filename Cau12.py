# Câu 12. Cài đặt thuật toán tìm bội chung nhỏ nhất (BCNN) của một tập hợp số nguyên bất kỳ.

import math
def bcnn(a, b):
    return abs(a * b) // math.gcd(a, b)
def bcnn_tap_hop(arr):
    result = arr[0]
    for num in arr[1:]:
        result = bcnn(result, num)
    return result
arr = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
print(f"Bội chung nhỏ nhất của tập hợp số là: {bcnn_tap_hop(arr)}")
