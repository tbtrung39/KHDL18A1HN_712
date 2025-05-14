tong = 0
dong_le = 1

with open("dayso.dat", "r") as f:
    for dong in f:
        if dong_le % 2 == 1:  # Nếu dòng là dòng lẻ
            so = map(int, dong.strip().split())
            tong += sum(so)
        dong_le += 1

print("Tổng các số ở các hàng lẻ là:", tong)