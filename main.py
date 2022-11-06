import numpy as np
from numpy import *
import re

infile = open("input.dat", 'r')
data = infile.read()
infile.close()
virgula = re.sub(",", " ", data)

#se o arquivo de entrada estiver com virgulas, converte para espaco para leitura dos dados numericos
file1 = open("input.dat","w")
file1.write(virgula)
file1.close()

# x e y em arrays
x, y= loadtxt('input.dat', unpack=True)

def fibonacci(n):
   if n <= 2:
      return n - 1
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(0, len(x)):
  
  x[i] = fibonacci(x[i])

for i in range(0, len(y)):

  y[i] = math.factorial(y[i])


file2 = open("output.dat","w")

#Esse loop posiciona os dados para ficarem de acordo com o enunciado do projeto
for i in range(0, len(x)):

  z1 = str(x[i])
  z2 = str(y[i])
  n = str(i+1)

  array1 = "Linha " + n + ": Fib("+ "x" +")=" + z1 + " " + "Fact("+ "y" +")=" + z2 + "\n"
  file2.write(array1)


file2.close()
