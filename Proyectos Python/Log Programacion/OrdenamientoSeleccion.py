import random 
import os
os.system("cls")

"""
de los datos que faltan por ordenar, determinar el menor de ellos y 
ubicarlo de primero en ese conjunto de datos.
"""

def construyeVector(V,n,rango):
    V[0]=n
    for i in range(1,n+1):
        V[i]=random.randint(1,rango)

def imprimeVector(V,mensaje='vector sin nombre:\t'):
    print("\n",mensaje,end="")
    m=V[0]+1
    for i in range(1,m):
        print(V[i],end=",")
    print()
    
def intercambie(V,a,b):
    aux=V[a]
    V[a]=V[b]
    V[b]=aux
    
def ordenaAscen(V):
    for i in range(1,V[0]):
        k=i
        for j in range(i+1,V[0]+1):
            if V[j]<V[k]:
                k=j
        intercambie(V,i,k)           
tam=30
vec1=[0]*(tam+1)
construyeVector(vec1,16,99)
imprimeVector(vec1,"vector vec1:\t")
ordenaAscen(vec1)
imprimeVector(vec1,"vector vec2 despues de ordenarlo:\t")