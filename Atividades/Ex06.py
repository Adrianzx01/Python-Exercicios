#Escreva um programa que receba uma lista de nomes e imprima apenas os que começam com a letra "A".
nomes = ["Ana", "Bruno", "Amanda", "Carlos"]
nomes_com_a = [nome for nome in nomes if nome.startswith("A")]
print(nomes_com_a)
