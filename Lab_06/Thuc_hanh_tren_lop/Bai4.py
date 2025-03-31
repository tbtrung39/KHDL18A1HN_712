ds_so = []
while True:
    so = int(input("Nhập số: "))
    if so == 0:
        break
    ds_so.append(so)

ds_so[:0] = [[1, 2, 3]] 
ds_so.append([1, 2, 3]) 
if len(ds_so) > 5: 
    ds_so.insert(5, [1, 2, 3])

vi_tri_k = int(input("Nhập số k: "))
if 0 <= vi_tri_k <= len(ds_so):  
    ds_so.insert(vi_tri_k, vi_tri_k)
else:
    print(f"Không thể chèn {vi_tri_k} vào vị trí {vi_tri_k} vì danh sách có {len(ds_so)} phần tử.")

print("Danh sách sau khi chèn:", ds_so)
