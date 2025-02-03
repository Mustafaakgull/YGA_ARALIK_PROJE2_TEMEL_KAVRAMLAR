num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))
operation = input("İşlem seçin (toplama, çıkarma, çarpma, bölme): ").lower()

result = None

if operation == "toplama":
    result = num1 + num2
elif operation == "çıkarma":
    result = num1 - num2
elif operation == "çarpma":
    result = num1 * num2
elif operation == "bölme":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Bir sayıyı sıfıra bölemezsiniz!")
else:
    print("Geçersiz işlem.")

if result is not None:
    print(f"Sonuç: {result}")

with open("sonuclar.txt", "a") as file:
    file.write(f"{num1} {operation} {num2} = {result}\n")
