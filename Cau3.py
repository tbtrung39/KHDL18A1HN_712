# Câu 3. Kiểm tra số đối xứng
# a) Nhập một số nguyên và kiểm tra xem nó có đối xứng không.
# b) Tìm số đối xứng lớn nhất nhỏ hơn một số nhập vào.
# c) Kiểm tra xem số có dạng xyyx hay không.

# a) 
def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]

n = int(input())
if la_so_doi_xung(n):
    print(f"Số {n} là số đối xứng.")
else:
    print(f"Số {n} không phải là số đối xứng.")
print()

# b) 
def so_doi_xung_lon_nhat(n):
    for i in range(n-1, 0, -1):
        if la_so_doi_xung(i):
            return i
    return None

n = int(input())
result = so_doi_xung_lon_nhat(n)
if result:
    print(f"Số đối xứng lớn nhất nhỏ hơn {n} là: {result}")
else:
    print(f"Không có số đối xứng nào nhỏ hơn {n}.")
print()

# c) 
def la_so_xyyx(n):
    s = str(n)
    return len(s) == 4 and s[0] == s[3] and s[1] == s[2]

n = int(input())
if la_so_xyyx(n):
    print(f"Số {n} có dạng xyyx.")
else:
    print(f"Số {n} không có dạng xyyx.")
