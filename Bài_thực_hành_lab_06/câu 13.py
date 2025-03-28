chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]

# Tạo tất cả các tổ hợp có thể
cac_cau = [f"{cn} {dt} {tn}" for cn in chu_ngu 
                          for dt in dong_tu 
                          for tn in tan_ngu]

print("Tất cả các câu có thể:")
for i, cau in enumerate(cac_cau, 1):
    print(f"{i}. {cau}")