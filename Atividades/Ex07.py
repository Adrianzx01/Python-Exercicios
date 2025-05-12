#Crie uma função que receba uma string e conte quantas vogais ela contém.
def contar_vogais(texto):
    return sum(1 for letra in texto.lower() if letra in "aeiou")

print(contar_vogais("Python é divertido"))
