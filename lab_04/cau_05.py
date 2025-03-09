
def nhap_so():
    while True:
        so = int(input("Nhập một số (nhập số âm để dừng): "))
        if so < 0:
            print("Số âm đã được nhập, chương trình dừng lại.")
            break
        else:
            print(f"Số bạn đã nhập: {so}")
nhap_so()
