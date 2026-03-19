saldo = float(input("Digite o seu saldo: "))
saque = float(input("Digite o valor do saque: "))


def saldo_final (saldo,saque):

    if saque > saldo:
      return "saldo invalido"


    if saque <1000:
        taxa = saque * 0.02
        saldo -= (saque + taxa)
        
    else:
        saldo -= saque
    return saldo

print ("Saldo restante:", saldo_final(saldo, saque))