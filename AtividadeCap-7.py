#7.1 - 
n=['Ana', 'joão', 'jose', 'joão', 'jose', 'Ana']
Ana=n.count('Ana')
joão=n.count('joão')
jose=n.count('jose')

d={'Ana' : Ana, 'joão' :joão, 'jose' : jose}

for  i,j in d.items():
     print('Nome :', i, ' : ', j, 'vezes')


#7.2 -



#7.3 - 
n=str(input('Digite uma frase: '))

x=n.split()

for i in x:
    j=i.islower()
    subst=str(i)
    if j != True:
        impressao = n.replace(subst,'*')

print(impressao)

#7.4 -



#7.5- 
n=int(input('Informe um numero: '))

x=list()

for i in range(n):
    y=int(input('Informe valor pra lista: '))
    x.append(y)
print(x)


#7.6 -
n=int(input('Informe um numero: '))

x=list()

for i in range(n):
    y=int(input('Informe valor pra lista: '))
    x.append(y)
print(x)

soma=0
maior=x[0]
menor=x[0]
for i in x:
    soma +=i

    if menor > i:
        menor=i
    if maior < i:
        maior=i

print('Soma: ', soma)
print('Media: ', soma/n)
print('Maior: ', maior)
print('Menor: ', menor)