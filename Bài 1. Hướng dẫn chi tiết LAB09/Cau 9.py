# Cau 9.
def hanoi_tower(n, from_column, to_column, using_column):
    if n == 1:
        print("Dich chuyen dia 1 tu cot", from_column, "den cot", to_column)
        return
    hanoi_tower(n-1, from_column, using_column, from_column)
    print("Dich chuyen dia", n, "tu cot", from_column, "den cot", to_column)
    hanoi_tower(n-1, using_column, to_column, from_column)

n = int(input("Nhap vao so dia can chuyen: "))
hanoi_tower(n, "A", "B", "C")