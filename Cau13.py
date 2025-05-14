# Câu 13. Tìm hai số nguyên tố liên tiếp có khoảng cách xa nhất trong khoảng từ 1 đến N.

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def tim_so_nguyen_to_lien_tiep_cach_xa_nhat(N):
    last_prime = None
    max_distance = 0
    prime_pair = (0, 0)

    for i in range(2, N + 1):
        if la_so_nguyen_to(i):
            if last_prime is not None:
                distance = i - last_prime
                if distance > max_distance:
                    max_distance = distance
                    prime_pair = (last_prime, i)
            last_prime = i

    return prime_pair, max_distance
N = int(input())
prime_pair, max_distance = tim_so_nguyen_to_lien_tiep_cach_xa_nhat(N)
print(f"Hai số nguyên tố liên tiếp có khoảng cách xa nhất là {prime_pair[0]} và {prime_pair[1]}. Khoảng cách là {max_distance}.")
