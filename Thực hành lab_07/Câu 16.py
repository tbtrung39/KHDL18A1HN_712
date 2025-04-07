#Câu 16:
a=list(map(int,input("Nhập dãy số nguyên, cách nhau bởi dấu cách:").split()))
n=len(a)
pairs = [(i,j) for i in range(n) for j in range(i,n) if a[i]+1 == a[j]]
print("các cặp chỉ số thỏa mãn điều kiện:",pairs)