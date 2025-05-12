def tim_cuc_tri(path_in, path_out):
    with open(path_in, 'r') as file:
        numbers = list(map(int, file.read().split()))
    
    cuc_tri = []
    for i in range(1, len(numbers) - 1):
        if (numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]) or \
           (numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]):
            cuc_tri.append(numbers[i])
    with open(path_out, 'w') as file:
        file.write(str(len(cuc_tri)) + '\n')
        file.write(' '.join(map(str, cuc_tri)))
path_in = input("Nhập đường dẫn đến file đầu vào (VD: f_in.dat): ")
path_out = "f_out.dat"
tim_cuc_tri(path_in, path_out)
print(f"Đã ghi kết quả vào {path_out}")
