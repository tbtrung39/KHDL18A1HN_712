with open("PASSENGERS.IN", "w") as f:
    f.write("5\n")
    f.write("20.5\n")
    f.write("1.3 1.5 3.5 2 3\n")
    f.write("7.25 3.5 7\n")
    f.write("11 7 4.5 10 8.5 6\n")
    f.write("13\n")

def read_passenger_data(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        passengers = [list(map(float, line.split())) for line in lines[1:]]
    return passengers

def process_passengers(passengers):
    weights = []
    canceled = []
    for i, bags in enumerate(passengers):
        total = sum(bags)
        weights.append(total)
        if len(bags) > 5 or total > 23:
            canceled.append(i + 1)
    return weights, canceled

def write_results(weights, canceled):
    with open("WEIGHT.OUT", "w") as f:
        for w in weights:
            f.write(f"{w:.2f}\n")
    with open("CANCELED.OUT", "w") as f:
        for idx in canceled:
            f.write(str(idx) + "\n")

passengers = read_passenger_data("PASSENGERS.IN")
weights, canceled = process_passengers(passengers)
write_results(weights, canceled)

print("Tổng trọng lượng hành lý mỗi hành khách:")
for w in weights:
    print(f"{w:.2f}")
print("Hành khách bị hủy chuyến (số thứ tự):", canceled)