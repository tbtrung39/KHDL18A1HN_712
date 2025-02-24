a = int(input('Nhập vào hệ số a, b, c\n\ta = '))
b = int(input('\tb = '))
c = int(input('\tc = '))
print(f'Phương trình bậc hai {a}x\u00b2 + {b}x + {c} = 0: ', end='')

delta = b**2 - 4*a*c
if delta < 0:
    print('Vô nghiệm')
elif delta == 0:
    x = (-b)/(2*a)
    print('Có nghiệm kép x\u2081 = x\u2082 =', round(x, 2))
else:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print('Có 2 nghiệm x\u2081 =', round(x1, 2), '; x\u2082 =', round(x2, 2))