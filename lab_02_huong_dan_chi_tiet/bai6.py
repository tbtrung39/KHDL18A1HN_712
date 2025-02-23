print("\n\n\t\t===================MENU===================")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
print("\n\t\t====================END=====================")
print('Hay nhap lua chon cua ban (1-->4): ', end = "")
luachon = int(input())
if luachon == 1:
    print("Ban da lua chon the loai phim tinh cam")
elif luachon == 2:
    print("Ban da lua chon the loai phim kinh di")
elif luachon == 3:
    print("Ban da lua chon the loai phim hoat hinh")
elif luachon == 4:
    print("Ban da lua chon the loai phim khoa hoc vien tuong")
else:
    print("Ban da lua chon sai. Vui long kiem tra lai")