def bai_11():
    n = int(input("Nhập số sinh viên n: "))
    c_plus = set(map(int, input("Nhập số thứ tự sinh viên dự thi C++ (cách nhau bằng space): ").split()))
    java = set(map(int, input("Nhập số thứ tự sinh viên dự thi Java (cách nhau bằng space): ").split()))
    python = set(map(int, input("Nhập số thứ tự sinh viên dự thi Python (cách nhau bằng space): ").split()))
    chi_1 = (c_plus - java - python) | (java - c_plus - python) | (python - c_plus - java)
    hai_ngon_ngu = ((c_plus & java) - python) | ((c_plus & python) - java) | ((java & python) - c_plus)
    ca_3_ngon_ngu = c_plus & java & python
    print("Sinh viên chỉ thi một ngôn ngữ:", sorted(chi_1))
    print("Sinh viên thi hai ngôn ngữ:", sorted(hai_ngon_ngu))
    print("Sinh viên thi cả ba ngôn ngữ:", sorted(ca_3_ngon_ngu))
bai_11()
