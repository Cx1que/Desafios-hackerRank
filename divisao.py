"""
Adicione lógica para imprimir duas linhas. A primeira linha deve conter o resultado da divisão inteira,  a//b . A segunda linha deve conter o resultado da divisão real,  a/b .
Nenhum arredondamento ou formatação é necessário.
"""

if __name__ == '__main__':
    a = int(input('a: '))
    b = int(input('b: '))
    
    print(a // b)
    print(a / b)