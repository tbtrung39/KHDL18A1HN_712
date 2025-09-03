s=input("Nhap van ban: ")
c=0
t=False
for x in s:
    if x.isalnum():
        if not t:
            c+=1
            t=True
    else:
        t=False
print("so tu: ",c)