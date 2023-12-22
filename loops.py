"""
O trecho de código fornecido lê um número inteiro, n, da entrada padrão (STDIN). Para todos os números inteiros não negativos i < n, imprima i**2.

A lista de números inteiros não negativos que são menores que n = 3 é [0, 1, 2]. Imprima o quadrado de cada número em uma linha separada."""
if __name__ == '__main__':
    n = int(input('numero: '))
    for i in range(0, n):       # a cada iteração de i, de 0 até n-1
        result = i**2           # i**2 é guardada na váriavel result
        print(result, end="\n") # imprime a variavel result a cada iteração, com quebras de linhas
        