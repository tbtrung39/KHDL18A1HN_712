listA = [0,0.3,5.8,12,15,8.5,7.0]
with open('Dulieu.dat','w') as f:
    for number in listA:
        f.write(str(number)+ '\n')