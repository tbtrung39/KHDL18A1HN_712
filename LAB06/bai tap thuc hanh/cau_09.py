nums = list(map(int, input("Nhap danh sach so, cach nhau boi dau cach: ").split()))
assert all(num % 2== 0 for num in nums), "Danh sach chua so le!"
print("Danh sach hop le:", nums)