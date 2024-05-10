#Calculadora em python nativo
#Feito por Henrique

Numero1 = input('Qual o número: ')
Numero2 = input('Qual o outro número: ')
Operação = input('Qual operação deseja fazer: ')
soma = int(Numero1) + int(Numero2)
menos = int(Numero1) - int(Numero2)
vezes = int(Numero1) * int(Numero2)
dividir = int(Numero1) / int(Numero2)

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

#Números com virgula não são possiveis colocar, apenas os resultados podem ter virgula.
