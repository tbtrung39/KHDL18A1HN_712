balance = 0
while True:
    transaction = input()
    if not transaction:
        break
    action, amount = transaction.split()
    amount = int(amount)
    if action == 'D':
        balance += amount
    elif action == 'W':
        balance -= amount
print(balance)
