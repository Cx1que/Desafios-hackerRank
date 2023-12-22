"""Dada a folha de pontuação dos participantes para o seu Dia do Desporto Universitário, é necessário encontrar a pontuação do segundo classificado. Você recebe pontuações. Guarde-os em uma lista e encontre a pontuação do vice-campeão. """
n = int(input("Informe : n"))
arr = map(int, input(" ").split()) 

placar=list(set(arr))  # remove os valores duplicados e cria uma nova lista placar a partir da lista arr
placar.remove(max(placar)) # remove o valor maximo da lista placar
print(max(placar)) # imprime o agora maior valor da lita placar


        