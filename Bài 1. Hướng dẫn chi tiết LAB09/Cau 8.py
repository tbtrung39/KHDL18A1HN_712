# Cau 8.
def find_solutions(n, x1, x2, x3):
    if x1 + x2 + x3 == n:
        print(x1, x2, x3)
        return
    if x1 + x2 + x3 < n:
        find_solutions(n, x1 + 1, x2, x3)
        find_solutions(n, x1 , x2 + 1, x3)
        find_solutions(n, x1 , x2 , x3 + 1)
N = int(input("Nhap so N:"))
print("Cac nghiem cua phuong trinh N = x1 + x2 + x3 la: ")
find_solutions(N, 0, 0, 0)