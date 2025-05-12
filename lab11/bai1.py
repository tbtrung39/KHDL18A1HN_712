with open('dayso.dat','w')as f :
    f.write('4 5 6\n7 8 9\n10 11')
def tinh_tong_day_so(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            numbers = [int(num) for num in data]
            
            tong_tat_ca = sum(numbers)
            
            tong_le = sum(num for num in numbers if num % 2 != 0)
            
            print(f"Tổng các số trong file là: {tong_tat_ca}")
            print(f"Tổng các số lẻ trong file là: {tong_le}")
    except FileNotFoundError:
        print("Không tìm thấy file!")
    except ValueError:
        print("File có chứa dữ liệu không hợp lệ!")
tinh_tong_day_so('dayso.dat')