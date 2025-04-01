data = []
while True:
    try:
        line = input("Nhập giao dịch (D/W số tiền) hoặc nhấn Enter để kết thúc: ")
        if not line:
            break
        data.append(line)
    except EOFError:
        break


transactions = [int(x.split()[1]) if x.split()[0] == 'D' else -int(x.split()[1]) for x in data]
balance = sum(transactions)


print(balance)