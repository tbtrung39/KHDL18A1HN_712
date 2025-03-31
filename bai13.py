# Danh sách các chủ ngữ, động từ và tân ngữ
chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]

# Tạo tất cả các câu kết hợp từ các phần tử trong danh sách
for subject in chu_ngu:
    for verb in dong_tu:
        for object in tan_ngu:
            # In câu kết hợp
            print(f"{subject} {verb} {object}")
