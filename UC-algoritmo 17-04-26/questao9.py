notas = [5, 8, 9, 6, 10]
contador = 0

for nota in notas:
    if nota > 7:
        contador += 1
        
print(f"O resultado é {contador}")