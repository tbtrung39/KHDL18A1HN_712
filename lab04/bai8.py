
print("Nhập một chữ cái (A-Z hoặc a-z):")
ch = input()
while len(ch) != 1 or not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z')):
    print("Vui lòng nhập một chữ cái hợp lệ!")
    ch = input()
ascii_value = -1 
i = 65 
while i <= 122:
    if i == 65 and ch == "A":
        ascii_value = 65
    elif i == 66 and ch == "B":
        ascii_value = 66
    elif i == 67 and ch == "C":
        ascii_value = 67
    elif i == 68 and ch == "D":
        ascii_value = 68
    elif i == 69 and ch == "E":
        ascii_value = 69
    elif i == 70 and ch == "F":
        ascii_value = 70
    elif i == 71 and ch == "G":
        ascii_value = 71
    elif i == 72 and ch == "H":
        ascii_value = 72
    elif i == 73 and ch == "I":
        ascii_value = 73
    elif i == 74 and ch == "J":
        ascii_value = 74
    elif i == 75 and ch == "K":
        ascii_value = 75
    elif i == 76 and ch == "L":
        ascii_value = 76
    elif i == 77 and ch == "M":
        ascii_value = 77
    elif i == 78 and ch == "N":
        ascii_value = 78
    elif i == 79 and ch == "O":
        ascii_value = 79
    elif i == 80 and ch == "P":
        ascii_value = 80
    elif i == 81 and ch == "Q":
        ascii_value = 81
    elif i == 82 and ch == "R":
        ascii_value = 82
    elif i == 83 and ch == "S":
        ascii_value = 83
    elif i == 84 and ch == "T":
        ascii_value = 84
    elif i == 85 and ch == "U":
        ascii_value = 85
    elif i == 86 and ch == "V":
        ascii_value = 86
    elif i == 87 and ch == "W":
        ascii_value = 87
    elif i == 88 and ch == "X":
        ascii_value = 88
    elif i == 89 and ch == "Y":
        ascii_value = 89
    elif i == 90 and ch == "Z":
        ascii_value = 90
    elif i == 97 and ch == "a":
        ascii_value = 97
    elif i == 98 and ch == "b":
        ascii_value = 98
    elif i == 99 and ch == "c":
        ascii_value = 99
    elif i == 100 and ch == "d":
        ascii_value = 100
    elif i == 101 and ch == "e":
        ascii_value = 101
    elif i == 102 and ch == "f":
        ascii_value = 102
    elif i == 103 and ch == "g":
        ascii_value = 103
    elif i == 104 and ch == "h":
        ascii_value = 104
    elif i == 105 and ch == "i":
        ascii_value = 105
    elif i == 106 and ch == "j":
        ascii_value = 106
    elif i == 107 and ch == "k":
        ascii_value = 107
    elif i == 108 and ch == "l":
        ascii_value = 108
    elif i == 109 and ch == "m":
        ascii_value = 109
    elif i == 110 and ch == "n":
        ascii_value = 110
    elif i == 111 and ch == "o":
        ascii_value = 111
    elif i == 112 and ch == "p":
        ascii_value = 112
    elif i == 113 and ch == "q":
        ascii_value = 113
    elif i == 114 and ch == "r":
        ascii_value = 114
    elif i == 115 and ch == "s":
        ascii_value = 115
    elif i == 116 and ch == "t":
        ascii_value = 116
    elif i == 117 and ch == "u":
        ascii_value = 117
    elif i == 118 and ch == "v":
        ascii_value = 118
    elif i == 119 and ch == "w":
        ascii_value = 119
    elif i == 120 and ch == "x":
        ascii_value = 120
    elif i == 121 and ch == "y":
        ascii_value = 121
    elif i == 122 and ch == "z":
        ascii_value = 122 
    i += 1
if ascii_value != -1:
    print(f"Ký tự '{ch}' có giá trị ASCII là {ascii_value}")
else:
    print(f"Ký tự '{ch}' không hợp lệ!")
