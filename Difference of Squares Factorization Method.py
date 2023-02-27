# This code implements Fermat's Difference of Squares method of integer factorization.

import math

def IsItASquare(n):
  if math.sqrt(n)==int(math.sqrt(n)):
    return(True)
  else:
    return(False)

def Factor(n):
  c=[0,0]
  for k in range(int(math.sqrt(n))):
    if IsItASquare(n+k*k):
      c=[k, int(math.sqrt(n+k*k))]
  if c==[0,0]:
    print(str(n)+" is prime")
  else:
    print(str(n)+'='+str(c[1]-c[0])+'x'+str(c[1]+c[0]))


k = int(input())
Factor(k)
