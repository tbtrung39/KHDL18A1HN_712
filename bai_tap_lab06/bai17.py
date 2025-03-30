n = int(input("Nhập n: "))

ma_tran_don_vi = []
for i in range(n):
  hang = []
  for j in range(n):
    if i == j:
      hang.append(1)
    else:
      hang.append(0)
  ma_tran_don_vi.append(hang)

print(ma_tran_don_vi)