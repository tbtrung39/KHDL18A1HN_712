kw=float(input("nhap so kw: "))
if kw>0 or kw<=100:
    print("gia tien :%0.2f"%(2000*kw))
elif kw>=101 or kw<200:
    print("gia tien :%0.2f"%(2000*100)+(2500*(kw-100)))
elif kw>=201 or kw<300:
    print("gia tien :%0.2f"%(2000*100)+(2500*100)+3000*(kw-200))
elif kw>300:
    print("gia tien :%0.2f"%(2000*100+2500*100+3000*100)+5000*(kw-300))