a = float(input('\nInforme a primeira nota:'))
b = float(input('\nInforme a segunda nota:'))
c = float(input('\nInforme a terceira nota:'))
m = (a+b+c)/3
if m>=7:
    print('\nAprovado com media {:.1f}'.format(m))
elif m>=5 and m<7:
    print('\nRecuperacao com media {:.1f}'.format(m))
else:
    print('\nReprovado com media {:.1f}'.format(m))
