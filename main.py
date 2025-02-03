num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))
operation = input("İşlem seçin (toplama, çıkarma, çarpma, bölme): ").lower()

if operation == "toplama":
    print(f"Sonuç: {num1 + num2}")
elif operation == "çıkarma":
    print(f"Sonuç: {num1 - num2}")
elif operation == "çarpma":
    print(f"Sonuç: {num1 * num2}")
elif operation == "bölme":
    if num2 != 0:
        print(f"Sonuç: {num1 / num2}")
    else:
        print("sayı sıfıra bölünemez...")
else:
    print("Geçersiz işlem.")
