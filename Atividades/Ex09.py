#Escreva uma função que receba uma lista e retorne uma nova lista sem elementos duplicados.
def remover_duplicatas(lista):
    return list(set(lista))

print(remover_duplicatas([1, 2, 2, 3, 4, 4, 5]))
