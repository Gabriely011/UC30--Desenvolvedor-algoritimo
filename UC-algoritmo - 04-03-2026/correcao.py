#questão 1

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
produto = num1 * num2

print("Soma:", soma)
print("Produto:", produto) 


#questão 2

numero = int(input("Digite um número inteiro positivo: "))
if numero % 2 == 0:
    resultado = numero ** 2
else:
    resultado = numero ** 3

print("Resultado:", resultado) 

#questão 3 

nome = input ("Digite seu login: ")
senha = input ("Digite sua senha: ")

if (nome == "procopio" and senha =="12345") or (nome == "paiva" and senha == "54321"):
    print ("Seja Bem-Vindo!")
else: 
    print ("Usuário e senha não conferem")

#questão 4

nome = input("digite seu nome :")
senhaCorreta = "123456"

tentativa= 3

while tentativa > 0:
   senha = input("Digite sua senha")

   if senha == senhaCorreta:
       print (f"Olá, {nome}! Seja bem vindo!")
       break
else:
    tentativa -= 1

    if tentativa == 2:
        print("senha errada ! Você tem 2 tentativas")
    elif tentativa == 1:
        print("senha errada ! Você tem uma tentativa.")
        
    else:
        print("senha bloqueda!")
