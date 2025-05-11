#Escreva um programa que receba uma palavra e diga se ela é um palíndromo.
palavra = input("Digite uma palavra: ")
print("É palíndromo" if palavra == palavra[::-1] else "Não é palíndromo")