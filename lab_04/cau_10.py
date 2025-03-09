def so_to_chu(so):

    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    chuoi = ""
    for digit in str(so):  
        chuoi += don_vi[int(digit)] + " "  
    return chuoi.strip()  
def main():
    while True:
        try:
            so = input("Nhập một số thập phân:")
            if so.isdigit(): 
                so_chu = so_to_chu(so)
                print(f"Số {so} được viết thành chữ: {so_chu}")
                break
            else:
                print("Vui lòng nhập một số thập phân hợp lệ!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")
main()
