# Cau 3.
def countdown(seconds):
    if seconds == 0:
        print("Time's up!")
    elif seconds <= 120:
        print(seconds, "senconds left")
        countdown(seconds - 1)
print("Bat dau dem lui! ")
countdown(120)