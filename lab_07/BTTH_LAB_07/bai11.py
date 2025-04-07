so_cpp = int(input("So sinh vien C++: "))
so_java = int(input("So sinh vien Java: "))
so_python = int(input("So sinh vien Python: "))

tong = so_cpp + so_java + so_python
danh_sach = ["t" + str(i+1) for i in range(so_cpp)] + ["k" + str(i+1) for i in range(so_java)] + ["h" + str(i+1) for i in range(so_python)]

print("Danh sach sinh vien theo ngon ngu:")
print("C++:", danh_sach[:so_cpp])
print("Java:", danh_sach[so_cpp:so_cpp+so_java])
print("Python:", danh_sach[so_cpp+so_java:])
