import random
def tao_tap_hop_A():
    numbers = list(range(10))
    A = set(random.sample(numbers, 5))
    print("Danh sách ban đầu:", numbers)
    print("Tập hợp A gồm 5 phần tử ngẫu nhiên:", A)
tao_tap_hop_A()
