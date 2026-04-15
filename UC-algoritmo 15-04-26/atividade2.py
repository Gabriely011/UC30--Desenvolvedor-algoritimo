def calcularTotal():
    precos = []

    for i in range[2]:
        try:
            preco = float(input(f"Digite o preço do {i+1}º produto: "))
            precos.append(preco)
        except ValueError:
            print("Erro: os preços devem ser numéricas.")
            return
        
    total = sum(precos)
    print(f"O valor total da compra deu: R$ {total}")

calcularTotal()