def tim_cuc_tri_va_ghi_file():
    with open("f_in.dat", "r") as f:
        numbers = list(map(int, f.readline().strip().split()))
    
    cuc_tri = []
    
    for i in range(1, len(numbers) - 1):
        if (numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]) or \
           (numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]):
            cuc_tri.append(numbers[i])
    
    with open("f_out.dat", "w") as f:
        f.write(f"{len(cuc_tri)}\n")
        f.write(" ".join(map(str, cuc_tri)))

    print("Đã ghi số lượng và giá trị cực trị vào f_out.dat.")

with open("f_in.dat", "w") as f:
    f.write("1 3 2 5 6 4 7 6 8 9")

tim_cuc_tri_va_ghi_file()