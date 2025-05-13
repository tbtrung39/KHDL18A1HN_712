def tao_file_inp():
    with open('inp.txt', 'w') as f:
        f.write('5 3 9 1 8 7')

def sap_xep_file_inp():
    try:
        with open('inp.txt', 'r') as file_in:
            data = file_in.read().split()
            numbers = [int(num) for num in data]
        
        numbers.sort()
    
        with open('out.dat', 'w') as file_out:
            file_out.write(' '.join(str(num) for num in numbers))
        
        print("Đã sắp xếp xong! Kết quả đã ghi vào file out.dat.")
    except FileNotFoundError:
        print("Không tìm thấy file inp.txt!")
    except ValueError:
        print("File inp.txt có dữ liệu không hợp lệ!")

tao_file_inp()
sap_xep_file_inp()