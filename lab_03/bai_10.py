def phan_tich_thua_so_nguyen_to(n):
    """Phân tích thừa số nguyên tố của n."""
    if n <= 1:
        return "n phải là số nguyên dương lớn hơn 1"
    
    ket_qua = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            ket_qua.append(i)
    if n > 1:
        ket_qua.append(n)
    return ket_qua

# Ví dụ sử dụng
n = 28
print(f"Phân tích thừa số nguyên tố của {n}: {phan_tich_thua_so_nguyen_to(n)}")