import math
print('Bem-vindo ao programa que reolve P.G.')
print("""a1 = Primeiro Termo
q = Razão
n = quantidade de números
an = Ultimo Termo""")
oqqd = str(input('Digite oque você quer saber sobre a P.g.: '))
oqqdm = oqqd.upper()
if oqqdm == 'AN':
    q=int(input('Qual o valor de q: '))
    n=int(input('Qual o valor de n: '))
    a1=int(input('Qual o valor de a1: '))
    def A_N(q, n, a1):
        an= a1 + math.pow(q, (n - 1))
        return an
    print(f'O valor de an é equivalente a {A_N(q, n, a1):.1f}')
elif oqqdm == 'Q':
    a1 = int(input('Qual o valor de a1: '))
    n = int(input('Qual o valor de n: '))
    an = int(input('Qual o valor de an: '))
    def Q_Q(n, a1, an):
        q = math.pow(an / a1, 1 / (n - 1))
        return q
    print(f'O valor de q é equivalente a {Q_Q(n, a1, an):.1f}')
elif oqqdm == 'N':
    q=int(input('Qual o valor de q: '))
    an=int(input('Qual o valor de an: '))
    a1=int(input('Qual o valor de a1: '))
    def N_N(q, an, a1):
        nn = math.log(an / a1, q) + 1
        return nn
    print(f'O valor de n é equivalente a {N_N(q ,an, a1):.1f}')
elif oqqdm == 'A1':
    n = int(input('Qual o valor de n: '))
    an = int(input('Qual o valor de an; '))
    q = int(input('Qual o valor de q: '))
    def A_1(n, an, q):
        A1 = an / math.pow(q, (n - 1))
        return A1
    print(f'O valor de a1 é equivalente a {A_1(n, an, q):.1f}')
else:
    print('Voce escreveu errrado, reinicie o programa')
fechar_programa = str(input('OPressione <enter> para encerrar o programa!'))