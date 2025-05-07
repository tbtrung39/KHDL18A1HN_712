# Cau 9. Dvq
def giai_bai_tap_9(file_in='Bai_2_Thuc_hanh_phong_may/PASSENGERS.IN', file_weight='Bai_2_Thuc_hanh_phong_may/WEIGHT.OUT', file_cancel='Bai_2_Thuc_hanh_phong_may/CANCELED.OUT'):
    with open(file_in, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    n = int(lines[0])  
    passengers = lines[1:]

    weight_results = []
    canceled_list = []

    for idx, line in enumerate(passengers):

        items = list(map(float, line.split()))
        tong_kg = sum(items)
        so_kien = len(items)
        
        weight_results.append(f"{tong_kg:.2f}")
        
        if tong_kg > 23 or so_kien > 5:
            canceled_list.append(str(idx + 1)) 

    with open(file_weight, 'w') as f:
        for w in weight_results:
            f.write(w + '\n')

    with open(file_cancel, 'w') as f:
        for c in canceled_list:
            f.write(c + '\n')

 
    if canceled_list:
        print("Hanh khach bi huy chuyen(Vuot qua gioi han):")
        for c in canceled_list:
            print(f" - Hanh khach {c}")
    else:
        print("Khong co hanh khach nao bi huy chuyen.")

giai_bai_tap_9()