tap_ky_tu = set()
print("Nhap ky tu (bam ESC de ket thuc):")
while True:
    ky_tu = input()
    if ky_tu == 'ESC':
        break
    if not ky_tu.isdigit():
        tap_ky_tu.add(ky_tu)
print("Tap hop cac ky tu:", tap_ky_tu)
