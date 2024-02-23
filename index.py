# tupla é uma lista imutavel

# dados que não nunca vão ser alterados é utilizar tuplas ex:cpf,rg,etc

tupla=(10,100,20,30,20)
# tupla[0]=22
print(tupla[2])

# o python não tem uma variavel const como no javascript então caso queria declara uma variavel imutavel é colocar o nome dele em maisculos
# NOME=NICKOLAS
# É UMA CONSTANTE
# AGORA nome=Nickolas pode ser alterado 

text ="ola mundo"
print(text)
nova_lista=tuple(text.split(" "))
print(nova_lista)

# oque é o range range():Criar uma sequencia de números range(numero inicial,numero final)

for n in range(1,10):
    lista2 = []
    lista2.append(n)
    soma = sum(lista2)
    print(soma)

#
    

lista= range(1,10)
print(lista)

listaalfabeto = ["a", "b", "c", "d"]
letrasenumeradas = enumerate(listaalfabeto)

for indice, letra in letrasenumeradas:
  print(f"Índice: {indice} - Letra: {letra}")