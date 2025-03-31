import random
so_ngau_nhien = random.choice([x for x in range(201) if x % 5 == 0 and x % 7 == 0])
print(so_ngau_nhien)