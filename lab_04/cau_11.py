import os
print('\n MENU GOI MON')
while True:
    print('|1. Cafe|')
    print('|2. Cam vat|')
    print('|3. Nuoc ep carot|')
    print('|4. Nuoc loc|')
    print('|5. Nuoc dua|')

    chon=int(input('chon do uong: '))
    if chon==1:
        print("Ban da chon cafe.")
    elif chon ==2:
        print("Ban da chon cam vat")
    elif chon ==3:
        print("Ban da chon nuoc ep carot")
    elif chon==4:
        print("Ban da chon nuoc loc")
    elif chon ==5:
        print("Ban da chon nuoc dua")
    else:
        print('chi chon tu 1 den 5')
        break