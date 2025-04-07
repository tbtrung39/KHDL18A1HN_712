cpp = {"An", "Bình", "Châu"}
java = {"Châu", "Bình", "Duy"}
python = {"Bình", "Duy", "An"}

# Tìm sinh viên giỏi ít nhất 2 môn
at_least_2 = (cpp & java) | (cpp & python) | (java & python)

print("Sinh viên giỏi ít nhất 2 môn:", at_least_2)
