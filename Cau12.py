# Câu 12. Viết chương trình tìm số nhỏ nhất có thể biểu diễn thành tổng của ba số chính phương theo hai cách khác nhau.]

def is_square(n):
    return int(n**0.5) ** 2 == n

def tim_so_nho_nhat():
    sum_of_squares = {}
    
    for a in range(1, 100):
        for b in range(a, 100):
            for c in range(b, 100):
                sum_val = a*a + b*b + c*c
                if sum_val not in sum_of_squares:
                    sum_of_squares[sum_val] = [(a, b, c)]
                else:
                    sum_of_squares[sum_val].append((a, b, c))

    for num, ways in sum_of_squares.items():
        if len(ways) >= 2:
            return num, ways[0], ways[1]

    return None

result = tim_so_nho_nhat()
if result:
    num, way1, way2 = result
    print(f"Số nhỏ nhất là {num} và có thể biểu diễn như sau:")
    print(f"Cách 1: {way1[0]}^2 + {way1[1]}^2 + {way1[2]}^2")
    print(f"Cách 2: {way2[0]}^2 + {way2[1]}^2 + {way2[2]}^2")
else:
    print("Không tìm thấy số thỏa mãn.")
