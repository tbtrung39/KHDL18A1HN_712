n = int(input("Tổng số sinh viên: "))

ct = set(map(int, input("Danh sách sinh viên thi C++: ").split()))
java = set(map(int, input("Danh sách sinh viên thi Java: ").split()))
python = set(map(int, input("Danh sách sinh viên thi Python: ").split()))

all_students = ct | java | python

only_one = set()
only_two = set()
all_three = set()

for sv in all_students:
    count = (sv in ct) + (sv in java) + (sv in python)
    if count == 1:
        only_one.add(sv)
    elif count == 2:
        only_two.add(sv)
    elif count == 3:
        all_three.add(sv)

print("Sinh viên chỉ thi 1 ngôn ngữ:", only_one)
print("Sinh viên thi 2 ngôn ngữ:", only_two)
print("Sinh viên thi cả 3 ngôn ngữ:", all_three)
