def kiem_tra_loi(chuoi):
    for i in range(len(chuoi)-1):
        if chuoi[i]==chuoi[i+1]:
            raise Exception("lỗi nhập liệu(2 ký tự liên tiếp giống nhau)")
    for i in range(len(chuoi)-3):
        if chuoi[i]==chuoi[i+1]==chuoi[i+2]==chuoi[i+3]:
            raise Exception("lỗi nhập lặp lại(4 ký tự liên tiếp giống nhau)")
    tu=chuoi.split()
    for i in range(len(tu)-4):
        if tu[i]==tu[i+1]==tu[i+2]==tu[i+3]==tu[i+4]:
            raise Exception("lỗi nhập trùng lặp(5 tử giống nhau liên tiếp)")
try:
    chuoi=input("Nhập chuỗi ký tự:")
    kiem_tra_loi(chuoi)
    print("chuỗi hợp lệ. không phát hiện lỗi")
except Exception as e:
    print("phát hiện lỗi:",e) 
finally:
    print("chương trình tiếp tục hoạt động bình thường")
     
          
        