
numero1 = float(input("Digite o 1º numero"))
numero2 = float( input("Digite o numero 2º"))


def someProduto(numero1,numero2):
    soma = (numero1) + (numero2)
    multiplicacao = (numero1 * numero2)
    return soma, multiplicacao

resultado = someProduto (numero1, numero2)
print(f"O resultado é {resultado}")



