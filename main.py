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

for i in range(0, len(x)):
  #print(math.factorial(x[i]))
  x[i] = math.factorial(x[i])

for i in range(0, len(y)):
  #print(math.factorial(y[i]))
  y[i] = math.factorial(y[i])

DataSet = column_stack((x,y))
savetxt('output.dat', DataSet)