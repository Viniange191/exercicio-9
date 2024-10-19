lista1 = []
lista2 = []
jun = []
erro = []
print("lista 1")
for l in range(5):
    n = int(input("Digite um numero: "))
    lista1.append(n)
print("lista 2")
for l in range(5):
    n = int(input("Digite um numero: "))
    lista2.append(n)
for l in lista1:
    for o in lista2:
        if l == o:
            jun.append(o)
print(lista1)
print(lista2)
if jun == []:
    jun.append("não tem")
print(jun)

