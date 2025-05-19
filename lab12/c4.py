try:
    a,b = input("file nguon va dich:").split()
    open(b, 'w',encoding='utf-8').write(open(a,'r',encoding='utf-8').read())
    print("da sao chep")
except:
    print("loi khi xu li file.")