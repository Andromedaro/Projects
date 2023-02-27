# A mathematician whose name I've forgotten spent his whole life calculating lengths of periods of 1/n for n=2,3,...,1358246 but only in base 10 - or b=10 in the following functions.

import math

def A2(n,b): # Elementary school Division Algorithm for 1/n in base b
    D=b
    ar=[]
    remainders=[]
    r=0
    while True:
        if n>D:
            ar.append(0)
            D=D*b
        else:
            if (D%n) not in remainders:
                remainders.append(D%n)
                ar.append(math.floor(D/n))
                D=(D%n)*b
            else:
                r=1
                break
        if (D%n == 0):
            ar.append(math.floor(D/n))
            break
    return(ar,r)

def A3(n,b): # Length of repeating section of base expansion
    A = A2(n,b)
    if A[1]==0:
        return(0)
    else:
        return(len(A[0]))

def A4(n,b): # Length of repeating portion of base expansion when dividing 1/k in base b for k=2,...,n
    ar=[]
    for k in range(2,n+1):
        ar.append(A3(k,b))
    return(ar)

def A5(r,b): # List of integers k up to r which are equal to the length of the repeating sequence of 1/k in base b
    ar=[]
    for k in range(2,r):
        if A3(k,b)==k:
            ar.append(k)
    return(ar)
        
b=11
k=7
r=200
A=A2(k,b)

print("Digits to the right of the dot when calculating 1/"+str(k) + " in base " +str(b) +": "+str(A[0]))
if A[1] == 1:
    print("and this sequence repeats")

print("\n"+"Length of repeating portion of base expansion when dividing 1/n in base "+str(b)+" for n=2,3,...,"+str(r))
s=A4(r,b)
for g in s:
    print(g, end="  ")
