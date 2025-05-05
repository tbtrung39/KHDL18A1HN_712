from hinhhoc import is_TamGiac, ChuviTamGiac, S_TamGiac
from hinhhoc import ChuviHinhvuong, Dien_tich_hinh_vuong

def main():
    print("Tam giác:")
    a, b, c = 3, 4, 5
    if is_TamGiac(a, b, c):
        print(f"Chu vi tam giác ({a}, {b}, {c}): {ChuviTamGiac(a, b, c)}")
        print(f"Diện tích tam giác: {S_TamGiac(a, b, c):.2f}")
    else:
        print("Không phải là tam giác.")

    print("\nHình vuông:")
    canh = 5
    print(f"Chu vi hình vuông cạnh {canh}: {ChuviHinhvuong(canh)}")
    print(f"Diện tích hình vuông: {Dien_tich_hinh_vuong(canh)}")
main()
