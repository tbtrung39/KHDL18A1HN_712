# Cau 5.
'''
# Cach 1.
from ntpath import join


def sum_recursive(n, result, current_sum, current_list):
    if current_sum == n:
        print(n, '=', current_list)
        return
    for i in range(1, n + 1):
        if current_sum + i <= n:
            sum_recursive(n,result, current_sum +i, current_list + [i])
n = int(input("Nhap so tu  nhien N: "))
sum_recursive(n, [], 0, [])
'''
# Cach 2.
def sum_recursive(n, result):
    current_sum = 0
    current_list = []
    def helper(n, current_sum, current_list):
        if current_sum == n:
            result.append(current_list)
            return
        for i in range(1, n +1):
            if current_sum + i <= n:
                helper(n, current_sum + i, current_list + [i])
    helper(n, current_sum, current_list)
    return result

n = int(input("Nhap so tu nhien N: "))
result = sum_recursive(n , [])
for item in result:
    print("%d = %s" %(n, "+".join(map(str, item))))