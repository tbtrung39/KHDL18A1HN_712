a = int(input("Số sinh viên C++: "))
b = int(input("Số sinh viên Java: "))
c = int(input("Số sinh viên Python: "))
tong = a + b + c
ds = ["t" + str(i+1) for i in range(a)] + ["k" + str(i+1) for i in range(b)] + ["h" + str(i+1) for i in range(c)]
print("Danh sách sinh viên theo ngôn ngữ:")
print("C++:", ds[:a])
print("Java:", ds[c:c+b])
print("Python:", ds[c+c:])