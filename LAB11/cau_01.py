def tong_so_o_vi_tri_le():
    numbers = []
    
    with open("dayso.dat", 'r') as f:
        for line in f:
            nums_in_line = list(map(int, line.strip().split()))
            numbers.extend(nums_in_line)
    
    tong = sum(numbers[i] for i in range(0, len(numbers), 2))
    
    return tong

# Gọi hàm
ket_qua = tong_so_o_vi_tri_le()
print("Tổng các số ở vị trí lẻ trong dãy là:", ket_qua)