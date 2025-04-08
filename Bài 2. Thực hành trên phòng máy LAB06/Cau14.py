# Câu 14
import re

mat_khau = input("Nhap mat khau: ")

# Kiem tra do dai mat khau tu 6 den 12 ky tu
if 6 <= len(mat_khau) <= 12 and \
   re.search("[a-z]", mat_khau) and \
   re.search("[0-9]", mat_khau) and \
   re.search("[A-Z]", mat_khau) and \
   re.search("[$#@]", mat_khau):
    print("Mat khau hop le")
else:
    print("Mat khau khong hop le")