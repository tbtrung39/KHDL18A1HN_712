def calculate_electricity_cost(time_seconds):
 voltage = 220 # V
 current = 2.7 # A
 power = voltage * current # W
 energy_kWh = (power * time_seconds) / (1000 * 3600) # Chuyển đổi sang kWh
 cost = energy_kWh * 7000 # Giá 7000 đ/kWh
 return round(cost, 2)
time_seconds = int(input("Nhập thời gian sử dụng (giây): "))
print(f"Tiền điện phải trả: {calculate_electricity_cost(time_seconds)} VND")