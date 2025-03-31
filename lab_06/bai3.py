lst = [2,-4,1,9,-3,-6,3,-2,8]
duong = [x for x in lst if x > 0]
khac = [x for x in lst if x < 0]
lst_moi = duong + khac

print("Danh sách sau khi chuyển số dương lên đầu :", lst_moi)