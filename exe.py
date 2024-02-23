# pares

for x in range(2,21,2):
    print(x)

#mutiplos de 5
    soma=0
    for i in range(5,51,5):
        soma+=i
    print(f"{soma}")
#type
    # numer_='nickolas'
    # numero=1
    # numero2=2.1
    # numero3=True
    # print(type(numer_))
    # print(type(numero2))
    # print(type(numero3))
    # print(type(numero))
#saudação
    client=["jorge","oliver","nickolas","carlos"]

    for i in client:
        print("olá bem vindo "+i)
#impares de 1 a 10 e em seguida calcule e imprima a média desses números
    
    numbers=[]
    for i in range(1,10,2):
        numbers.append(i)
        soma=sum(numbers)
    print(soma/len(numbers))
