n1 = (int(input('Qual sua 1° nota? ')))
n2 = (int(input('Qual sua 2° nota? ')))
n3 = (int(input('Qual sua 3° nota? ')))
s=n1+n2+n3
nf=s/3
if(nf>=6):
    print ('Aprovadado com a média {:.2f}'.format(nf))
else:
    print ('Reprovado com a média {:.2f}'.format(nf))
