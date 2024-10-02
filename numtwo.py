def fibonacci_sequence(n):
    # gera a sequência de fibonacci até o n-ésimo número

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def is_in_fibonacci(num):
    # verifica se um número pertence à sequência de fibonacci
    if num < 0:
        return False
    # gerar a sequência de fibonacci até que o maior número seja maior ou igual ao num
    fib_sequence = fibonacci_sequence(num + 2)  # gera um pouco mais para garantir que chegue no num
    return num in fib_sequence

# valor defindo pela entraada do usuário
try:
    number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if is_in_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
