altura = float(input("Digite sua altura"))
altura = altura * 100

print(f"Sua altura é de {altura}cm")
print ("Sua altura é de:", altura)

nome = "Gaby"
idade= 16
texto= "meu nome é {} e tenho {} anos".format (nome,idade)
texto= "Meu nome é %se tenho %d" % (nome,idade)
texto="Meu nome é {n} e tenho %d anos".format(n=nome,i=idade)
print(texto)

