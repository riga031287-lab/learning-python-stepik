n = int(input())
d1 = n //1000
d2 = (n//100) % 10
d3 = (n //10) % 10
d4 = n % 10
if d1 + d4 == d2 - d3:
    print("Да")
else: 
    print("Нет")