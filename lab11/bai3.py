def l(a,i):
    return(a[i] > a[i-1] and a[i] > a[i+1] )or(a[i]<a[i-1] and a[i]<a[i+1])
with open("f_in.dat","r") as f:
    a= list(map(int,f.read().split()))

cuctri=[]
for i in range(1,len(a)-1):
    if l(a,i):
        cuctri.append(a[i])
with open("f_out.dat","w") as f:
    f.write(str(len(cuctri))+"\n")
    f.write(' '.join(map(str,cuctri)))