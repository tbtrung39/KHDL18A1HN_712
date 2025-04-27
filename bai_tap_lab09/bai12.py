def solve(chicken, dog):
    if chicken + dog == 36 and chicken * 2 + dog * 4 == 100:
        print(f"Số gà: {chicken}, Số chó: {dog}")
    elif chicken + dog > 36 or chicken < 0 or dog < 0:
        return
    else:
        solve(chicken + 1, dog)

solve(0, 36)
