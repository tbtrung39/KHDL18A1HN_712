def tao_list_chan():
    return list(filter(lambda x: x % 2 == 0, range(11, 101)))

lst_chan = tao_list_chan()
print("Danh sách số chẵn từ 11 đến 100:", lst_chan)
