def so_chan_trong_khoang():
    return list(filter(lambda x: x % 2 == 0, range(1, 101)))

print("Các số chẵn từ 1 đến 100:", so_chan_trong_khoang())