d=int(input(''))
k=int(input(''))
#90 por dia para 100km e para cada km 12 conto a mais
if k>(100*d):
    valor=(90*d+(k-100*d)*12)
elif k<=(100*d):
    valor=90*d
print('{:.2f}'.format(valor))