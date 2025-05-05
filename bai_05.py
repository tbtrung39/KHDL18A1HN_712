import random

def tao_tap_hop_ngau_nhien_chu_so():
    """Tạo tập hợp 5 phần tử ngẫu nhiên từ danh sách chữ số."""
    danh_sach_chu_so = [str(i) for i in range(10)]
    tap_hop_ngau_nhien = set(random.sample(danh_sach_chu_so, 5))
    return tap_hop_ngau_nhien

if __name__ == "__main__":
    tap_hop_a = tao_tap_hop_ngau_nhien_chu_so()
    print("Tập hợp A gồm 5 phần tử ngẫu nhiên:", tap_hop_a)