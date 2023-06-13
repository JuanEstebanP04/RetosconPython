import random 
import os
os.system("cls")
"""
Busqueda en un vector con datos ordenados
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
                 
def ordenaAscen(V):
    for i in range(1,V[0]):
        for j in range(1, V[0]-i + 1):
            if V[j]>V[j+1]:
                intercambie(V,j,j+1) 

def intercambie(V,a,b):
    aux=V[a]
    V[a]=V[b]
    V[b]=aux
    
def busbin(V,d):
    inicio=1
    fin=V[0]
    while inicio<fin:
        mitad=(inicio+fin)//2
        if V[mitad]==d:
            return mitad
        if d<V[mitad]:
            fin=mitad-1
        else:
            inicio=mitad+1
    return -1
    
tam=30
vec1=[0]*(tam+1)
construyeVector(vec1,16,99)
ordenaAscen(vec1)
imprimeVector(vec1,"vector vec1:\t")
busqueda=int(input("Ingrese el numero que quiere buscar:"))  
encontrar=busbin(vec1,busqueda)
print(encontrar)



    