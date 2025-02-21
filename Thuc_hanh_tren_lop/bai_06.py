def read_three_digit_number(num):
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if num < 100 or num > 999:
        return "Số không hợp lệ! Vui lòng nhập số có 3 chữ số."
    
    hundred = num // 100
    ten = (num // 10) % 10
    unit = num % 10

    result = f"{units[hundred]} trăm"
    if ten == 0 and unit != 0:
        result += " lẻ"
    elif ten != 0:
        result += f" {tens[ten]}"
    if unit != 0 and not (ten == 1 and unit == 0):
        result += f" {units[unit]}"
    
    return result

num = int(input("Nhập số nguyên có ba chữ số: "))
print(read_three_digit_number(num))