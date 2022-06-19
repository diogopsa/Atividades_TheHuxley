s = float(0)
t = int(0)
n = int(0)
while n != 999:
    n = int(input(''))
    if n > 2 and n != 999:
        v = float(((n-2)*12.89))
        s = (s + v)
        t = t+1
print('{:.2f}'.format(s))
print(t)
