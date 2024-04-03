a= float(input('Digite o rpimeiro valor de a:'))
b= float(input('Digite o rpimeiro valor de b:'))
c= float(input('Digite o rpimeiro valor de c:'))
delta = (b**b)-4*a*c
print ("\n**********************************************\n")
if a==0:
    print('Essa conta não é possivel responder')
elif delta<0:
    print('Essa conta não é possivel responder')
else:
    x1=(-b+delta**(1/2))/(2*a)
    x2=(-b-delta**(1/2))/(2*a)
print("x1: {:.2f}, x2: {:.2f}". format(x1,x2))
