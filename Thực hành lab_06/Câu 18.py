#Câu 18:
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))

ma_tran = []
for i in range(m):
  hang = input(f"Nhập hàng thứ {i+1} (các số cách nhau bởi dấu cách): ").split()
  hang = [int(x) for x in hang]
  ma_tran.append(hang)

tong = 0
for hang in ma_tran:
  for phan_tu in hang:
    tong += phan_tu

print("Ma trận đã nhập:", ma_tran)
print("Tổng các phần tử:", tong)