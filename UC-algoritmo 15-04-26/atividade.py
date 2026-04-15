def media_aluno(): 
    
    notas = []
      
    try:
        for i in range(3):   
            nota = float(input(f"Nota {i+1}: "))
            notas.append(nota)
        media = sum(notas) / len(notas)
        print(f"Média: {media:.2f}")

    except ValueError:
        print("Notas devem ser números!")
    except ZeroDivisionError: 
        print("Sem notas!")

media_aluno()