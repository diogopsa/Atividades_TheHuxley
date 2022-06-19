contador = int(0)
v1=int(0)
v2=int(0)
v3=int(0)
v4=int(0)
while contador<7:
    anuncio = str(input(''))
    if anuncio == 'Rádio':
        frequencia=str(input(''))
        if frequencia == 'AM':
            valor = int(300)
            v1 = valor + v1
        else:
            valor = int(500)
            v1 = valor + v1
    elif anuncio == 'TV':
        horario = float(input(''))
        if horario > 20:
            valor = int(2000)
            v2 = valor + v2
        else:
            valor = int(1200)
            v2 = valor + v2
    elif anuncio == 'Revista':
        valor = int(750)
        v3 = valor + v3
    else:
        valor = int(1500)
        v4 = valor + v4
    contador +=1
valor_final = (v1+v2+v3+v4)
print('{:.2f}'.format(valor_final))
