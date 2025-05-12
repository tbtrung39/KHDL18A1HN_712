def sort_and_write(input_file, output_file):
    with open(input_file, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))

    numbers.sort()

    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, numbers)))

sort_and_write(r"bai_tap\Inp.txt", 'Out.dat')