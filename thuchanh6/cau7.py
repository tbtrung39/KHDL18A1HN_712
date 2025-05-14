List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for x in List:
    print(x)

b = [x[1] for x in List]
print(b)

import random
List.append(random.choice(List))

s = 0
for x in List:
    if x[0] in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]:
        s += x[1]
print(s)
