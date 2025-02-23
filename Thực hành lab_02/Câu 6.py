#Câu 6 :
n = int(input("nhập vào số nguyên có 3 chữ số:"))
if n <100 and n>999:
    print("số không hợp lệ hãy nhập lại")
else:
    hang_tram = n//100
    hang_chuc = (n//10)%10
    hang_don_vi = n % 10
    if hang_chuc == 0 and hang_don_vi == 0:
        print(hang_tram,"trăm")
    elif hang_chuc == 1 and hang_don_vi == 0:
        print(hang_tram,"trăm mười")
    elif hang_chuc == 0 and hang_don_vi!=0 :
        print(hang_tram,"trăm lẻ",hang_don_vi)
    elif hang_don_vi == 0 and hang_chuc!= 0 :
        print(hang_tram,"trăm",hang_chuc,"mươi")
    else:
        print(hang_tram,"trăm",hang_chuc,"mươi",hang_don_vi)    