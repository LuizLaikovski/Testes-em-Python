pt= int(input('Digite o valor do primeiro termo:'))
rz= int(input('Digite o valor da razão:'))
nt= int(input('Digite o valor do numero de termos:'))
def calcular_progressao_aritmetica(a1, razao, n):
    """
    Calcula os termos de uma progressão aritmética.

    Args:
    a1 (float): Primeiro termo da progressão.
    razao (float): Razão da progressão.
    n (int): Número de termos a serem calculados.

    Returns:
    list: Uma lista contendo os termos da progressão aritmética.
    """
    progressao = []
    termo_atual = a1
    for _ in range(n):
        progressao.append(termo_atual)
        termo_atual += razao
    return progressao

# Exemplo de uso:
primeiro_termo = pt
razao = rz
numero_de_termos = nt

progressao_aritmetica = calcular_progressao_aritmetica(primeiro_termo, razao, numero_de_termos)
print("Progressão aritmética:", progressao_aritmetica)
print("\n*****************************\n")
if rz<0:
    print("Essa P.A. é Decrescente")
elif rz==0:
    print("Essa P.A. é Constante")
else:
    print("Essa P.A. é Crescente")

