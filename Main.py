#Calculadora em python nativo
#Feito por Henrique

Numero1 = input('Qual o número: ')
Numero2 = input('Qual o outro número: ')
Operação = input('Qual operação deseja fazer: ')

soma = float(Numero1) + float(Numero2)
menos = float(Numero1) - float(Numero2)
vezes = float(Numero1) * float(Numero2)
dividir = float(Numero1) / float(Numero2)

if Operação == 'soma':
    print(f'O resultado é {soma}')
    print('Não use para fazer contas complexas!')
elif Operação == 'menos':
    print(f'O resultado é {menos}')
    print('Não use para fazer contas complexas!')
elif Operação == 'vezes':
    print(f'O resultado é {vezes}')
    print('Não use para fazer contas complexas!')
elif Operação == 'dividir':
    print(f'O resultado é {dividir}')
    print('Não use para fazer contas complexas!')
else:
    print('ERRO')

#Não use está calculadora para fazer contas grandes, pois ela é bem simples e não consegue fazer isso.
#Ela funciona com números com virgula