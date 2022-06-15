#Dados tr�s n�meros em ponto flutuante
# queremos saber quantos deles est�o acima da m�dia aritm�tica.
s=int(0)
k=int(0)
t=int(0)
a=float(input(''))
b=float(input(''))
c=float(input(''))
m=((a+b+c)/3)
if a>m:
    s=(s+1)
if b>m:
    k=(k+1)
if c>m:
    t=(t+1)
v=(s+k+t)
print(v)