binary_dict = {i: bin(i)[2:] for i in range(1, 101)}

# In thử một số dòng đầu
for i in range(1, 11):
    print(f"{i} -> {binary_dict[i]}")
