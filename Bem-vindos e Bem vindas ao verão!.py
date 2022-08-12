a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if b > a and b >= c:
    print(':(')
elif b > a and c > b and (abs(c-b)<abs(b-a)):
    print(':(')
elif a > b and b > c and (abs(c-b)>=abs(b-a)):
    print(':(')
elif a == b and b >= c:
    print(':(')
else:
    print(':)')