def tinh_S1(n):
    if n == 1:
        return 1
    return n + tinh_S1(n - 1)

def tinh_S2(n):
    if n == 1:
        return 1
    return n**2 + tinh_S2(n - 1)

def main():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            raise ValueError("n phải là số nguyên dương lớn hơn 0.")
        
        s1 = tinh_S1(n)
        s2 = tinh_S2(n)
        print(f"S1 = 1 + 2 + ... + {n} = {s1}")
        print(f"S2 = 1^2 + 2^2 + ... + {n}^2 = {s2}")
    
    except ValueError as ve:
        print(f"Lỗi giá trị: {ve}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == "__main__":
    main()
