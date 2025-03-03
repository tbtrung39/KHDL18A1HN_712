def tim_so_hoan_hao(n):
    """Tìm các số hoàn hảo nhỏ hơn n."""
    ket_qua = []
    for num in range(2, n):
        tong_uoc = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                tong_uoc += i + num // i
        if tong_uoc == num:
            ket_qua.append(num)
    return ket_qua

# Ví dụ sử dụng
n = 1000
print(f"Các số hoàn hảo nhỏ hơn {n} là: {tim_so_hoan_hao(n)}")