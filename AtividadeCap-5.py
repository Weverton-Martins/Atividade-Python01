#5.1 - 
n=float(input('Digite um valor em reais: '))

notas100=0
notas50=0
notas10=0
notas1=0

while n >=1:
    if n-100 >= 0:
        notas100 +=1
        n-=100

    elif n-50 >= 0:
        notas50 +=1
        n-=50
    elif n-10 >= 0:
        notas10 +=1
        n-=10
    elif n-1 >= 0:
        notas1 +=1
        n-=1
    
print('Notas de 100: ',notas100,'\nNotas de 50: ',notas50,'\nNotas de 10: ',notas10, '\nNotas de 1: ',notas1)

#5.2 -
n=float(input('Digite um valor de tempo: '))

Horas=0
Minutos=0
Segundos=0

while n >=1:
    if n-3600 >= 0:
        Horas +=1
        n-=3600
    elif n-60 >= 0:
        Minutos +=1
        n-=60
    elif n-1>= 0:
        Segundos +=1
        n-=1
        
print(Horas)
print(Minutos)
print(Segundos)

#5.3 - 
x=float(input('Digite um número: '))
y=float(input('Digite outro número: '))

Soma= x+y
Subtração= x-y
Multiplicação= x*y
Divisão= x/y

print('Resultado +: ',Soma)
print('Resultado -: ',Subtração)
print('Resultado *: ',Multiplicação)
print('Resultado /: ',Divisão)
