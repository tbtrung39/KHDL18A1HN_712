with open("Inp.txt", "r") as f:
    dong = f.readline() 
    day_so = list(map(int, dong.strip().split())) 

day_so.sort()

with open("out.dat", "w") as f:
    f.write(" ".join(map(str, day_so)))  