# Câu 10. Sử dụng break và continue
# a) Dừng vòng lặp khi gặp số chia hết cho 4.
# b) Bỏ qua số chia hết cho 6 trong vòng lặp.

# a)
for i in range(1, 21):
    if i % 4 == 0:
        print(f"Vòng lặp dừng tại số {i} vì chia hết cho 4.")
        break

print()

# b)
for i in range(1, 21):
    if i % 6 == 0:
        continue
    print(i, end=" ")
