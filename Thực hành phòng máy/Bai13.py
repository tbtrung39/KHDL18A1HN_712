
chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]
cau_tao_thanh = [f"{cn} {dt} {tn}." for cn in chu_ngu for dt in dong_tu for tn in tan_ngu]
for cau in cau_tao_thanh:
    print(cau)
