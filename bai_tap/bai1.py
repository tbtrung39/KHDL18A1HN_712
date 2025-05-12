def sum_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            print(f"Dòng: {numbers}, Tổng: {sum(numbers)}")

sum_lines(r"bai_tap\dayso.dat")
