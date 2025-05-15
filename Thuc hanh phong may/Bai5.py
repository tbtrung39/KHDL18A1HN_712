import doicoso

try:
    n = int(input("Nhập một số nguyên: "))

    nhi_phan = doicoso.doi_sang_nhi_phan(n)
    bat_phan = doicoso.doi_sang_bat_phan(n)
    thap_luc_phan = doicoso.doi_sang_thap_luc_phan(n)

    print(f"Số {n} ở hệ nhị phân là: {nhi_phan}")
    print(f"Số {n} ở hệ bát phân là: {bat_phan}")
    print(f"Số {n} ở hệ thập lục phân là: {thap_luc_phan}")

except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
