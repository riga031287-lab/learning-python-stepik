num = int(input())

# Выделяем цифры
first = num // 1000
second = (num % 1000) // 100
third = (num % 100) // 10
fourth = num % 10

# Проверяем условие
if first + fourth == second - third:
    print("ДА")
else:
    print("НЕТ")