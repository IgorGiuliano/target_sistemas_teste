def verifica_fibonacci(numero):
  # Gera a sequência de Fibonacci
    sequencia = [0, 1]
    while sequencia[-1] < numero:
        sequencia.append(sequencia[-1] + sequencia[-2])

    # Verifica se o número está na sequência
    return numero in sequencia

numero = int(input("Informe um número: "))
if verifica_fibonacci(numero):
    print(f"O número {numero} faz parte da sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO faz parte da sequência de Fibonacci.")