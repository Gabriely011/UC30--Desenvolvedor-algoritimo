pontos = int(input("Digite seus pontos: "))
derrotas = int(input("Digite o numero de derrotas: "))

def rank_jogador (pontos,derrotas): 
    pontos_finais = pontos - (derrotas * 10) 

    if pontos_finais < 0:
       return "Banido"
    elif pontos_finais < 100:    
       return "Bronze"
    elif pontos_finais < 300:
       return "Prata"
    elif pontos_finais < 600:
       return "Ouro"
    else:
       return "Diamante"

print(rank_jogador(pontos, derrotas))