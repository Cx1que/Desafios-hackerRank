"""
Dado um número inteiro, n, execute as seguintes ações condicionais:

Se n for ímpar, imprima Estranho
Se n for par e estiver no intervalo inclusivo de 2 a 5, imprima Não Estranho
Se n for par e estiver no intervalo inclusivo de 6 a 20, imprima Estranho
Se n for par e maior que 20, imprima Não Estranho"""

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input('n: ').strip())
    
if n % 2 !=0 :
  print("Weird")
elif n % 2 == 0 and 2<= n < 5:
  print("Not Weird")
elif n % 2 ==0 and 6<= n <=20 :
  print("Weird")
elif n%2==0 and n > 20:
   print("Not Weird")
else:
    print("Weird")