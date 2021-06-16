print("Epoca de eleiçoes!")


candidatoA = int(input("O Candidato A recebeu quantos votos? "))
candidatoB = int(input("Quantos votos recebeu o Candidato B? "))
candidatoC = int(input("Digite o numero de votos recebidos pelo Candidato C: "))
vBranco = int(input("Digite o total dos votos em branco: "))
vNulo = int(input("Digite o numero de votos nulos: "))

nEleitores = candidatoA + candidatoB + candidatoC + vBranco + vNulo
pVotosA = (100 * candidatoA) / nEleitores
pVotosB = (100 * candidatoB) / nEleitores
pVotosC = (100 * candidatoC) / nEleitores
pBrancos = (100 * vBranco) / nEleitores
pNulos = (100 * vNulo) / nEleitores

print("O numero total de eleitores foram ", nEleitores, " pessoas")
print("O primero candidato obteve ", pVotosA, "% dos votos totais!")
print("O Candidato B obteve ", pVotosB, "% dos votos totais!")
print("O terceiro candidato obteve ", pVotosC, "% dos votos totais!")
print("Os votos brancos tiveram ", pBrancos, "% dos votos totais!")
print("Ja os votos anulados, obtiveram  ", pNulos, "% dos votos totais!")
