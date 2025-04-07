d = {i: str(bin(i))[2:] for i in range(1, 101)}
print("Từ điển số và nhị phân:")
for k, v in d.items():
    print(f"{k}: {v}")