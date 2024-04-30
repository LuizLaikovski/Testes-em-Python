import random

while True:
    #define oque o computador vai escolher
    def escolha_computador():
        numero_gerado = int(random.randint(1, 3))
        return (numero_gerado)

    #define o numero escolhido pelo usuario
    def escolha_usuario():
        print("""Escolha uma das opções:
        [1]     Pedra
        [2]     Papel
        [3]     Tesoura""")
        numero_usuario = int(input('>>> '))
        return (numero_usuario)

    #defimição da escolha
    escolha_do_usuario = int(escolha_usuario())
    escolha_do_computador = int(escolha_computador())

    #definição dos nomes dos numeros
    if escolha_do_usuario == 1:
        escolha_do_usuario_2 = 'Pedra'
    elif escolha_do_usuario == 2:
        escolha_do_usuario_2 = 'Papel'
    elif escolha_do_usuario == 3:
        escolha_do_usuario_2 = 'Tesoura'

    if escolha_do_computador == 1:
        escolha_do_computador_2 = 'Pedra'
    elif escolha_do_computador == 2:
        escolha_do_computador_2 = 'Papel'
    elif escolha_do_computador == 3:
        escolha_do_computador_2 = 'Tesoura'

    #define o resultado
    print(f'Voce escolheu {escolha_do_usuario_2}, e o computador escolheu {escolha_do_computador_2}')
    if escolha_do_computador == 1:
        if escolha_do_usuario == 1:
            print('Empate')
        elif escolha_do_usuario == 2:
            print('Voce ganhou!')
        elif escolha_do_usuario == 3:
            print('O computador venceu!!')
    elif escolha_do_computador == 2:
        if escolha_do_usuario == 1:
            print('O computador venceu!!')
        elif escolha_do_usuario == 2:
            print('Empate')
        elif escolha_do_usuario== 3:
            print('Voce ganhou!')
    elif escolha_do_computador == 3:
        if escolha_do_usuario == 1:
            print('Voce ganhou!')
        elif escolha_do_usuario == 2:
            print('O computador ganhou!!')
        elif escolha_do_usuario == 3:
            print('Empate')
    else:
        print('DIGITOU ERRADO SEU BURRO')

    #encerra o loop
    escolha_final = str(input('Digite "sair" para encerrar o programa: '))
    if escolha_final.lower() == 'sair':
        break