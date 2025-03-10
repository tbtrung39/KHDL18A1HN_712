so = int(input("Nhập một số nguyên dương: "))  
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]  
ket_qua = ""  

while so > 0:  
    chu = chu_so[so % 10]  
    if ket_qua == "":  
        ket_qua = chu  
    else:  
        ket_qua = chu + " " + ket_qua  
    so //= 10  

print("Dạng chữ của số:", ket_qua)  