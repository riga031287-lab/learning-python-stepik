print("===Конвертер валют===")
USD_RATE = 450.0
print("Выберите направление")
print("1 - Тенге (KZT) в Доллары (USD)")
print("2 -  Доллары (USD) в Тенге (KZT) ")
tenge = float (input("Введите сумму в тенге "))
usd = tenge / USD_RATE
print(f"{tenge:,.2f} ₸ ={usd: .2f} usd")
choise = input("Введите 1 или 2")
if choise =="1":
    tenge_str = input("Введите сумму в тенге")
    tenge = float(tenge_str)
    usd = tenge / USD_RATE
    print("Результат: " +  str(tenge) + "KZT  =" + str(usd) + "USD")
elif choise == "2":
    usd_str = input("Введите сумму в долларах: ")
    usd = float(usd_str)
    tenge = usd * USD_RATE
    print("Результат: " + str(usd) + " USD = " + str(tenge) + " KZT")
else:
    print("Ошибка: нужно ввести 1 или 2.")