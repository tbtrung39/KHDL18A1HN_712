#Câu 2:
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
def gcd_list(numbers, n):
    if n == 1:
        return numbers[0]
    return gcd(numbers[n-1],gcd_list(numbers,n-1))
