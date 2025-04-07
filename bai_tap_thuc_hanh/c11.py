n = int(input("Nhập số lượng sinh viên tham gia thi: "))

a = list(map(int, input("Nhập số thứ tự sinh viên thi C++: ").split()))
b = list(map(int, input("Nhập số thứ tự sinh viên thi Java: ").split()))
c = list(map(int, input("Nhập số thứ tự sinh viên thi Python: ").split()))

set_a = set(a)
set_b = set(b)
set_c = set(c)

only_cpp = set_a - set_b - set_c
only_java = set_b - set_a - set_c
only_python = set_c - set_a - set_b

cpp_java = set_a & set_b - set_c
cpp_python = set_a & set_c - set_b
java_python = set_b & set_c - set_a

cpp_java_python = set_a & set_b & set_c

print("Sinh viên chỉ thi C++:", only_cpp)
print("Sinh viên chỉ thi Java:", only_java)
print("Sinh viên chỉ thi Python:", only_python)

print("Sinh viên thi C++ và Java:", cpp_java)
print("Sinh viên thi C++ và Python:", cpp_python)
print("Sinh viên thi Java và Python:", java_python)

print("Sinh viên thi cả 3 ngôn ngữ:", cpp_java_python)