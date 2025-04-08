# Cau 3.
import random

tap_so = set()
while len(tap_so) < 10:
    so_ngau_nhien = random.randint(2, 99)
    tap_so.add(so_ngau_nhien)

print('Tap hop so:', tap_so)
print('Phan tu nho nhat:', min(tap_so))
print('Phan tu lon nhat:', max(tap_so))
print('Tong cac phan tu:', sum(tap_so))