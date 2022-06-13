ph = float(input('Digite o pH da solucao:'))
if ph > 7 and ph <= 14:
    print('\nEssa solucao e basica.')
elif ph == 7:
    print('\nEssa solucao e neutra.')
elif ph < 7 and ph > 0:
    print('\nEssa solucao e acida.')
else:
    print('\nValor deve estar entre 0 e 14.')