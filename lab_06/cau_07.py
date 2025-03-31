import random

List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], 
         ["sat", 128], ["sun", 120]]
print("Danh sách List_:")
for item in List_:
    print(item)
second_element_third_day = List_[2][1]  
print(f"\nGiá trị thứ hai của ngày thứ ba (wed) là: {second_element_third_day}")
print(f"\nĐộ dài của danh sách List_ hiện tại là: {len(List_)}")
new_day = random.choice(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
new_sale_value = random.randint(50, 150)
List_.append([new_day, new_sale_value])
print(f"Danh sách List_ sau khi thêm phần tử ngẫu nhiên: {List_}")
days_to_check = ["mon", "tue", "sat", "sun"]
total_sales = 0
for day, sale in List_:
    if day in days_to_check:
        total_sales += sale
print(f"\nTổng số tiền bán được trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật là: {total_sales}")
