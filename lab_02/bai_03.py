ngay = int(input('Nhập vào ngày thứ (1->7) trong tuần: '))
if 1 <= ngay <= 7:
    if ngay == 1: print('1. Sunday')
    elif ngay == 2: print('2. Monday')
    elif ngay == 3: print('3. Tuesday')
    elif ngay == 4: print('4. Wednesday')
    elif ngay == 5: print('5. Thursday')
    elif ngay == 6: print('6. Friday')
    else: print('7. Saturday')
else:
    print('Chỉ nhập số từ 1 đến 7')