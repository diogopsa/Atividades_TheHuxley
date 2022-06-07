n=int(0)
c=int(0)
while c<5:
    a=float(input('\nDigite um valor:'))
    if a<0:
       n=(n+1)
    c=(c+1)
print('\nForam digitados {} numeros negativos'.format(n))