from functools import reduce

if __name__ == "__main__":
    try:
        n = int(input("Nhập số lượng phần tử n cho danh sách: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương.")
        else:
            input_str = input(f"Nhập {n} số nguyên cách nhau bởi dấu cách: ")
            numbers = [int(x) for x in input_str.split()]
            if len(numbers) != n:
                print(f"Vui lòng nhập đúng {n} số.")
            else:
                even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
                sum_of_evens = reduce(lambda a, b: a + b, even_numbers, 0)
                print("Danh sách đã nhập:", numbers)
                print("Các số chẵn trong danh sách:", even_numbers)
                print("Tổng các số chẵn:", sum_of_evens)
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")