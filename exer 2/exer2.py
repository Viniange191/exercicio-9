med =float(0)
qua = int(input("Digite a quantidade de numeros que irá digitar: "))
l = int(0)
med= float(0)
t = int(0)
s = []
while (l<qua):
    n = int(input("Digite o numero: "))
    s.append(n)
    t = n + t
    med = t/qua
    l+=1

print(s)
print("A média total é: ",med)