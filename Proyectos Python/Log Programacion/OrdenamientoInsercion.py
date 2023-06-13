import random 
import os
os.system("cls")

"""
de los datos que faltan por ordenar, elegir el primero e insertarlo en el
conjunto de datos ya ordenado.
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
    for i in range(2,V[0]+1):
        d=V[i]
        j=i-1
        while j>0 and V[j]>d:
            V[j+1]=V[j]
            j=j-1
        V[j+1]=d
         
tam=30
vec1=[0]*(tam+1)
construyeVector(vec1,16,99)
imprimeVector(vec1,"vector vec1:\t")
ordenaAscen(vec1)
imprimeVector(vec1,"vector vec1 despues de ordenarlo:\t")