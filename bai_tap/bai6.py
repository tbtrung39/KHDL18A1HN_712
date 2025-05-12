def ghi_bang_so():
    matrix = [
        [4, 1133, 180, 5],
        [192, 168, 1, 254],
        [1, 1, 1, 233]
    ]
    with open(r"bai_tap\bangso.txt", 'w') as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + '\n')

ghi_bang_so()
