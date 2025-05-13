def read_fin_file(file_path):
    with open(file_path, 'r') as fin:
        n = int(fin.readline())
        numbers = []
        total_sum = 0
        for i in range(n):
            line = fin.readline().strip().split()
            line_sum = sum(map(float, line))
            numbers.append(line_sum)
            total_sum += line_sum
    with open('found.dat', 'w') as found_dat:
        found_dat.write(str(total_sum) + '\n')
        for i in range(n):
            found_dat.write(str(numbers[i]) + '\n')

path= input("Nhập đường dẫn đến file muốn đọc nội dung: path=")
read_fin_file(path)