def tim_diem_doi_xung(xyz):
    """Tìm điểm đối xứng qua các mặt phẳng."""
    oxy = (xyz[0], xyz[1], -xyz[2])
    oxz = (xyz[0], -xyz[1], xyz[2])
    oyz = (-xyz[0], xyz[1], xyz[2])
    return oxy, oxz, oyz

# Ví dụ sử dụng
xyz = (1, 2, 3)
oxy, oxz, oyz = tim_diem_doi_xung(xyz)
print(f"Đối xứng Oxy: {oxy}, Oxz: {oxz}, Oyz: {oyz}")