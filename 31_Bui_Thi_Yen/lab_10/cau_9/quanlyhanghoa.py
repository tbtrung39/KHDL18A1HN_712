
def nhap_hang():
    ma=input("ma hang:")
    ten=input("ten hang:")
    dv=input("don vi:")
    dg=float(input("don gia:"))
    sl=int(input("so luong:"))
    return {"ma":ma,"ten":ten,"dv":dv,"dg":dg,"sl":sl}
def tinh_tien(h):
    return h["dg"]*h["sl"]
def tinh_thue(h):
    return tinh_tien(h)*0.1
def sap_xep(dshh):
    return sorted(dshh,key=tinh_thue,reverse=True)
