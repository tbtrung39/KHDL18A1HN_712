# Dữ liệu chiều cao của các sinh viên
chieu_cao_str = """
161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163
162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170
"""

# Chuyển đổi chuỗi thành danh sách các số nguyên
chieu_cao = [int(h) for h in chieu_cao_str.strip().split()]

# a. Hỏi nhóm có bao nhiêu sinh viên?
so_sinh_vien = len(chieu_cao)
print(f"a. Nhóm có {so_sinh_vien} sinh viên.")

# b. Tính chiều cao trung bình của các sinh viên trong nhóm.
chieu_cao_trung_binh = sum(chieu_cao) / len(chieu_cao)
print(f"b. Chiều cao trung bình của các sinh viên trong nhóm là: {chieu_cao_trung_binh:.2f} cm.")

# c. Liệt kê các chiều cao khác nhau của sinh viên trong nhóm và in ra chiều cao trung bình của nhóm.
chieu_cao_khac_nhau = sorted(list(set(chieu_cao)))
print("c. Các chiều cao khác nhau của sinh viên trong nhóm là:", chieu_cao_khac_nhau)
print(f"   Chiều cao trung bình của nhóm là: {chieu_cao_trung_binh:.2f} cm.")