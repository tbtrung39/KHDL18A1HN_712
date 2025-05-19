try:
    with open(input("Nhap ten file: "),'r',encoding = 'utf-8') as f:
        open(r"",'w',encoding='utf-8').write(f.read())
        print("da sao chep vao copy dat")
except:
    print("loi file ko ton tai hoac ko doc duoc")
    