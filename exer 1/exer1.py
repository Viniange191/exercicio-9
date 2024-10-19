n = int(input("digite um numero:"))
l = []
for i in range(1,n+1):
    l.append(i)
    for c in l:
        print(c,end=" ")
    print(" ")