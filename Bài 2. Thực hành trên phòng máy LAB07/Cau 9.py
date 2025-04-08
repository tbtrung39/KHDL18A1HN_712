# Cau 9.
n = int(input("Nhap so tu nhien n: "))

tap_uoc = {i for i in range(1, n + 1) if n % i == 0}
tap_khong_uoc = {i for i in range(1, n + 1) if n % i != 0}

print("Tap hop uoc cua n:", tap_uoc)
print("Tap hop khong la uoc cua n:", tap_khong_uoc)