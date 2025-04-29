def dao_nguoc_so(n):
    if n < 10:
        print(n,end = '')
    else:
        print(n%10,end='')
        dao_nguoc_so(n//10)

so = int(input("Nhập số nguyên dương : "))
dao_nguoc_so(so)