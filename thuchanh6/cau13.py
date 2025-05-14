subjects = ["Anh", "Em"]
verbs = ["Chơi", "Yêu"]
objects = ["Bóng đá", "Bóng rổ"]

sentences = [f"{subject} {verb} {object}" for subject in subjects for verb in verbs for object in objects]
for sentence in sentences:
    print(sentence)
