# Cau 7.Dvq
with open('Bai_1_Huong_dan_chi_tiet/Data.txt','r') as file:
    data=file.readlines()
    latin_chars = []
    numeric_chars = []
    for line in data:
        LT = []
        Num = []
        for char in line:
            if char.isalpha() and char.isascii():
                LT.append(char)
            elif char.isnumeric():
                Num.append(char)
        LT.append('\n')
        latin_chars.append(LT)
        numeric_chars.append(Num)
    with open('Bai_1_Huong_dan_chi_tiet/Latinh.txt','w') as f1:
        for sublist in latin_chars:
            f1.write(''.join(map(str,sublist)))
    with open('Bai_1_Huong_dan_chi_tiet/Chuso.txt','w') as f2:
                for item in numeric_chars:
                    for element in item:
                        f2.write(element)
