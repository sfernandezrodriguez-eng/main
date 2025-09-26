n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n=range(n1,n2+1)
for i in n:
    conversor=i%2
    if conversor==0:
        print(i,"es par")
