nomes = ["Ana","Bruno","Carlos","Diana"]
print("Nomes:",nomes)

nomes.remove("Bruno")
print("Lista atuaçizada:", nomes)

removido = nomes.pop()
print(f"Removido:{removido}")
print("Após pop()",nomes)

del nomes[0]
print("Após del nomes [0]",nomes)
