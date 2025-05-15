list_1 = input("Nhap cac phan tu list1 (cach nhau boi dau cach): ").split()
list_2 = input("Nhap cac phan tu list2 (cach nhau boi dau cach): ").split()

tu_dien = {f"<{a}>": f"<{b}>" for a, b in zip(list_1, list_2)}

print("Tu dien:")
for k, v in tu_dien.items():
    print(f"{k}: {v}")