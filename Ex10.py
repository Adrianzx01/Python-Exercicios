#Crie um programa que leia um número inteiro e diga se ele é primo ou não.
num = int(input("Digite um número: "))
if num < 2:
    print("Não é primo")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Não é primo")
            break
    else:
        print("É primo")