# Câu 3. Sử dụng break và continue
# a) Dừng vòng lặp khi gặp số chia hết cho 5.
# b) Bỏ qua số chia hết cho 3 trong vòng lặp.
# c) In các số từ 1 đến 10 nhưng bỏ qua số 7.

# a.
for i in range(1, 21):
    if i % 5 == 0:
        break
    print(i)

# b.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# c.
for i in range(1, 11):
    if i == 7:
        continue
    print(i)
