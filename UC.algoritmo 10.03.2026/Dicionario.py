# sem dicionario

matricula1 = 2026001
nome1 = "Ana Silver"
telefone1 = "98842-7940"

# com dicionario

aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva",
    "telefone": "98842-7940"
}

print (aluno)

contato = {
    "@riviamirelle": "Rivia Mirelle",
    "@clarateixeira" : "Maria C",
    "@gabrielypereira" : "Gabriely P",
    "@ericasantos" : "Erica S"
} 

print(contato)
print(type(contato))

# Acesso direto
print(contato["@riviamirelle"])

# Acesso seguro com get()
print(contato.get("@clarateixeira"))
print(contato.get("@gabrielypereira"))
print(contato.get("@ericasantos", "Não encontrado")) 


# add novo elemento

contato ["@riviamirelle"] = "Rivia"
print("Após add: ", contato)

# atualiza elemento existente 

contato.update({
        "@clarateixeira": "Maria Clara",
        "@riviamirelle": "Rivia M"
}) 

print("Após atualização:", contato)

# pop: remove e retorna

removido = contato.pop("@ericasantos")
print(f"Removida: {removido}")
print("Após o pop", contato)

#del remove sem retornar

del contato["@riviamirelle"]
print("Após del: ", contato)

#clear esvazia tudo

copia = dict(contato)
contato.clear()
print("Após clear:", contato)
print("Cópia: ", copia)

print("Numero de contato: ", len(contato)) #tamanho dicio

# verificar existência
if "@joao" in contato: 
    print(f"Encontado: {contato['@joao']}")
 
if "@ericasantos" in contato:
    print("Existe")
else: 
    print("Não Existe.")
