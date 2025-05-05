import random
import string

def sinh_tap_hop_ngau_nhien(size):
    """Sinh một tập hợp ngẫu nhiên các ký tự chữ và số."""
    chars = string.ascii_letters + string.digits
    return set(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    size_a = random.randint(5, 15)  # Kích thước ngẫu nhiên cho tập hợp A
    size_b = random.randint(5, 15)  # Kích thước ngẫu nhiên cho tập hợp B

    tap_hop_a = sinh_tap_hop_ngau_nhien(size_a)
    tap_hop_b = sinh_tap_hop_ngau_nhien(size_b)

    print("Tập hợp A:", tap_hop_a)
    print("Tập hợp B:", tap_hop_b)

    phan_tu_chung = tap_hop_a.intersection(tap_hop_b)
    print("Các phần tử chung của A và B:", phan_tu_chung)