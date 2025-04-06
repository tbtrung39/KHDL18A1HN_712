c = int(input("Số sinh viên C++: "))
j = int(input("Số sinh viên Java: "))
p = int(input("Số sinh viên Python: "))
tong = c + j + p
ds = ["t" + str(i+1) for i in range(c)] + ["k" + str(i+1) for i in range(j)] + ["h" + str(i+1) for i in range(p)]
print("Danh sách sinh viên theo ngôn ngữ:")
print("C++:", ds[:c])
print("Java:", ds[c:c+j])
print("Python:", ds[c+j:])
