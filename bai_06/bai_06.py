def xu_ly_file():
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()

        # a. Hiển thị nội dung dòng đầu tiên và dòng thứ 3
        if len(lines) >= 1:
            print("Nội dung dòng đầu tiên:", lines[0].strip())
        if len(lines) >= 3:
            print("Nội dung dòng thứ ba:", lines[2].strip())

        # b. Hiển thị nội dung toàn bộ file
        print("\nNội dung toàn bộ file:")
        for line in lines:
            print(line.strip())

        # c. Tìm các số lẻ và ghi vào file ODD.txt với định dạng ma trận 4x4
        odd_numbers = []
        for line in lines[1:]:  # Bỏ qua dòng đầu tiên
            numbers_str = line.strip().split()
            for num_str in numbers_str:
                try:
                    num = int(num_str)
                    if num % 2 != 0:
                        odd_numbers.append(num)
                except ValueError:
                    pass  # Bỏ qua các phần tử không phải số

        with open("ODD.txt", "w") as odd_file:
            for i in range(4):
                row = []
                for j in range(4):
                    if i * 4 + j < len(odd_numbers):
                        row.append(str(odd_numbers[i * 4 + j]))
                    else:
                        row.append("0")
                odd_file.write(" ".join(row) + "\n")

        # d. In ra nội dung dòng cuối của file ODD.txt
        try:
            with open("ODD.txt", "r") as odd_file_read:
                odd_lines = odd_file_read.readlines()
                if odd_lines:
                    print("\nNội dung dòng cuối của file ODD.txt:", odd_lines[-1].strip())
                else:
                    print("\nFile ODD.txt không có nội dung.")
        except FileNotFoundError:
            print("\nFile ODD.txt không tồn tại.")

    except FileNotFoundError:
        print("File data.txt không tồn tại.")

if __name__ == "__main__":
    xu_ly_file()