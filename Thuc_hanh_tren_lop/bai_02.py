def convert_time(days, hours, minutes, seconds): 
total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds 
return total_seconds 
d = int(input("Nhập số ngày: ")) 
h = int(input("Nhập số giờ: ")) 
m = int(input("Nhập số phút: ")) 
s = int(input("Nhập số giây: ")) 
print(f"Tổng số giây: {convert_time(d, h, m, s)} giây")
