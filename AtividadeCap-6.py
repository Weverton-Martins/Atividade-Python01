#6.1 - 
n=int(input('Digite um numero da sequencia de fibonacci que voce quer imprimir: '))

f=1
x=0
y=0

for i in range (n):
    print(f)
    y=f
    f=x+f
    x=y


#6.2 -
print('Fatorial de 9:')

n=1

for i in range (1, 10):
    n *=i
print(n)

#6.3 - 
print('Fatorial de 9:')
n=1 ; x=1
while (x<=9):
    n *= x
    x += 1

print(n)

#6.4 - 
print('Selecione uma opção a seguir: \n 1-Adição, \n 2-Subtração, \n 3-Divisão, \n 4-Multiplicação')
n=int(input('Operação: '))

x=float(input('Digite um numero: '))
y=float(input('Digite outro numero: '))

if n==1:
    print(x+y)

elif n ==2:
    print(x-y)

elif n==3:
    print(x/y)

elif n==4:
    print(x*y)

else:
    print('Operação invalida')

#6.5
n=int(input('Digite até qual valor fatorial deseja imprimir: \n'))
 
x=n
y=n-1
 
for i in range (n-1):
    x=y*x
    y=y-1
if x == 0:
    x=1
print(x)

#6.6 - IF e Else
if == 1:
    foo (10) ;
    break
elif == 2:
    foo2 ( X ) ;
    break
elif == 3:
    foo (5) ;
    break ;
else :
    print('Erro')