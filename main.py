import numpy as np
from numpy import *
import re

infile = open("input.dat", 'r')
data = infile.read()
infile.close()
virgula = re.sub(",", " ", data)

#print(virgula)

file1 = open("input.dat","w")
file1.write(virgula)
file1.close()

x, y= loadtxt('input.dat', unpack=True)

def fibonacci(n):
   if n <= 2:
      return n - 1
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(0, len(x)):
  #print(math.factorial(x[i]))
  x[i] = fibonacci(x[i])

for i in range(0, len(y)):
  #print(math.factorial(y[i]))
  y[i] = math.factorial(y[i])

DataSet = column_stack((x,y))
savetxt('output.dat', DataSet)