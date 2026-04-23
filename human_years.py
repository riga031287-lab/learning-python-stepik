a = int(input())
b = int(input())
c = int(input())
n_max = max(a, b, c)
n_min = min(a, b, c)
n_mid = (a + b +c) - n_max - n_min
print(n_max)
print(n_mid)
print(n_min)