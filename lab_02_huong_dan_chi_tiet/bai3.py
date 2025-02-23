a, b, c = map(float, input('Nhập độ dài các cạnh: ').split(","))

if a + b <= c or b + c <= a or c + a <= b:
    print('Không phải là độ dài 3 cạnh của tam giác')
else:

    if a == b == c:
        print('Đây là tam giác đều')
    elif a == b or a == c or b == c:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print('Đây là tam giác vuông cân!')
        else:
            print('Đây là tam giác cân')
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('Đây là tam giác vuông')
    else:
        print('Đây là tam giác thường.')