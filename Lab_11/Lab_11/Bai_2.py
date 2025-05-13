def sap_xep_tu_file():
    with open("Inp.txt", "r") as f:
        line = f.readline()
        numbers = list(map(int, line.strip().split()))
    numbers.sort()
    with open("out.dat", "w") as f:
        f.write(" ".join(map(str, numbers)))

with open("Inp.txt", "w") as f:
    f.write("10 3 7 2 8 1")

sap_xep_tu_file()
print("Đã sắp xếp xong và ghi vào file out.dat.")
