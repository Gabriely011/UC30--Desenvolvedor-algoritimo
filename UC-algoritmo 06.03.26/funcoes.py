notas = [7.5,8.0,9.5,6.0,8.5]
print("Notas:", notas)

print("Menor:",min(notas))
print("Maior:", max(notas))
print("Soma", sum (notas))
print("Média", sum (notas)/ len(notas))

nomes = ["Adriana","Brenos","Carla","Daniel"]

print("Usando FOR simples:")
for nome in nomes:
    print(F"Olá,{nome}!")

print("\n Usando enumerate:")
for indice, nome in  enumerate (nome):
    print(f"posição{indice}:{nome}")

original=["A","B","C"]
copia = list(original)

print("Original:",original)
print("Cópia:",copia)
print("São iguais:",original == copia)