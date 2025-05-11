#Faça um programa que gere a sequência de Fibonacci até o décimo termo.
fib = [0, 1]
for _ in range(8):  # Já temos 2 elementos
    fib.append(fib[-1] + fib[-2])
print(fib)