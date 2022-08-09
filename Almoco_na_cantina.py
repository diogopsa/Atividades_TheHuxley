#Helena é dona de uma pequena cantina que fornece refeições para os universitários. 
#No cardápio de hoje, eles podem escolher entre lasanha (R$ 8,00) ou estrogonofe (R$ 11,00) 
#para comer, e entre refrigerante (R$ 3,00) ou suco (R$ 2,50) para beber. 
#Escreva um programa que receba como entrada as escolhas de cada cliente e exiba o valor 
#total a ser pago.
comida = str(input(''))
bebida = str(input(''))
if comida == 'lasanha' or comida == 'Lasanha':
    valor_comida = float(8)
else:
    valor_comida = float(11)
if bebida == 'suco' or bebida == 'Suco':
    valor_bebida = float(2.5)
else:
    valor_bebida = float(3)
valor_total = valor_comida + valor_bebida
print("{:.2f}".format(valor_total))