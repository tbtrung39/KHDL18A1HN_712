base_salary = 1350000
experience = int(input("Nhập số tháng công tác: "))

if experience < 12:
    factor = 2.34
elif experience < 36:
    factor = 3.33
elif experience < 60:
    factor = 3.66
else:
    factor = 3.99

salary = factor * base_salary
print(f"Lương của nhân viên: {salary} đồng")