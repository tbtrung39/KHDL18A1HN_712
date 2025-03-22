n = int(input("Nhao so n: "))
dem_uoc = 0
for i in range(1, n+1):
    if n%i == 0:
        dem_uoc += 1
if dem_uoc == 2:
    print(n, "La so nguyen to")
else:
    print(n,"Khong phai so nguyen to")
    for k in range(n-1,1,-1):
        dem_uoc_gan_nhat = 0
        for j in range(1, k+1):
            if k%j == 0:
                dem_uoc_gan_nhat += 1
        if dem_uoc_gan_nhat == 2:
            print("So nguyen to gan nhat <", n, "la",k)
            break