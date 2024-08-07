def calcular_media_e_classificao(nota1,nota2,nota3,nota4,nota5):
    
    media=(nota1+nota2+nota3+nota4+nota5)/5
    
    if media >=7:
       classificacao = "aprovado"
    elif media >=5:
         classificacao = "em recuperação"
    else:
        classificacao = "reprovado"

    return media, classificacao

nota1 = float(input("digite á sua nota:"))
nota2 = float(input("digite á sua nota:"))
nota3 = float(input("digite á sua nota:"))
nota4 = float(input("digite á sua nota:"))
nota5 = float(input("digite á sua nota:"))

media, classificacao = calcular_media_e_classificao(nota1,nota2,nota3,nota4,nota5)

print(f"média:{media:.2f}")
print(f"Classificação: {classificacao}")