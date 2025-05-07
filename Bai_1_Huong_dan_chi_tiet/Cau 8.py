# Cau 8.Dvq
import csv 
sinh_vien={
    '001001':{'ten_sv':'Nguyen Van A','gioi_tinh':True,'nam_sinh':'2000'},
    '001002':{'ten_sv':'Tran Thi B','gioi_tinh':False,'nam_sinh':'2001'},
    '001003':{'ten_sv':'Hoan Tuan C','gioi_tinh':True,'nam_sinh':'2002'},
    '001004':{'ten_sv':'Nguyen Thi D','gioi_tinh':False,'nam_sinh':'2003'}
}
def them_sinh_vien(file_name,sinh_vien):
    with open(file_name,'w',newline='') as f_out:
        fieldnames=['ma_sv','ten_sv','gioi_tinh','nam_sinh']
        writer=csv.writer(f_out)
        writer.writerow(fieldnames)
        for ma_sv, sv in sinh_vien.items():
            writer.writerow([ma_sv,sv['ten_sv'],sv['gioi_tinh'],sv['nam_sinh']])
them_sinh_vien('Bai_1_Huong_dan_chi_tiet/sinhvien.csv',sinh_vien)