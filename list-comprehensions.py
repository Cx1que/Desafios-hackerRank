"""
Você recebe três inteiros x, y e z representando as dimensões de um cuboide juntamente com um inteiro n. Imprima uma lista de todas as coordenadas possíveis fornecidas por zn(i, j, k) em uma grade 3D onde a soma de i + j + k não é igual a n. Aqui n <= 25. Por favor, use compreensões de lista em vez de vários loops, como um exercício de aprendizagem."""
x = int(input("Informe X: "))
y = int(input("Informe Y: "))
z = int(input("Informe Z: "))
n = input("Informe N: ")

# verifica se n é um inteiro
if not n.isdigit():
  print("O valor de N deve ser um número inteiro.")
  exit()

n = int(n)

x_list = range(x+1)
y_list = range(y+1)
z_list = range(z+1)


coordenadas = [[i, j, k] for i in x_list for j in y_list for k in z_list]

coordenadas = [coordenada for coordenada in coordenadas if sum(coordenada) != n]

coordenadas.sort()

print(coordenadas)

