# Câu 7

List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sach List_:")
for item in List_:
    print(item)
print("\nPhan tu thu hai cua sublist thu ba:", List_[2][1])
print("\nDo dai cua List_:", len(List_))
List_.append(["random_day", 100])  
print("Danh sach List_ sau khi them:", List_)
tong_sale = List_[0][1] + List_[1][1] + List_[5][1] + List_[6][1]
print("\nTong sale value trong cac ngay thu hai, thu ba, thu bay va chu nhat:", tong_sale)