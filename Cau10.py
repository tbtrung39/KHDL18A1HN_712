# Câu 10. Viết chương trình tìm số nhỏ nhất có thể biểu diễn thành tổng của ba số chính phương theo hai cách khác nhau.


tong_dict = {}

for a in range(50):
    for b in range(a, 50):       
        for c in range(b, 50):  
            tong = a*a + b*b + c*c  

            if tong in tong_dict:
                tong_dict[tong].append((a, b, c))
            else:
                tong_dict[tong] = [(a, b, c)]


for tong in sorted(tong_dict):  
    if len(tong_dict[tong]) >= 2:
        print("Số nhỏ nhất là:", tong)
        print("Hai cách biểu diễn là:")
        cach1 = tong_dict[tong][0]
        cach2 = tong_dict[tong][1]
        print(f"{cach1[0]}^2 + {cach1[1]}^2 + {cach1[2]}^2")
        print(f"{cach2[0]}^2 + {cach2[1]}^2 + {cach2[2]}^2")
        break 
