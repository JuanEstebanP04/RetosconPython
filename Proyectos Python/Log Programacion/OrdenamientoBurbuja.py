import random 
import os
os.system("cls")

"""
de los datos que faltan por ordenar, desplazar el mayor a que ocupe la última posición del conjunto de 
datos que falta por ordenar. La forma como se desplaza el mayor dato hacia la última posición es 
comparando dos datos consecutivos y ordenarlos ascendentemente, es decir, si el primer dato es mayor que el segundo,
se intercambian dichos datos, de lo contrario se dejan tal cual están
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
        for j in range(1, V[0]-i + 1):
            if V[j]>V[j+1]:
                intercambie(V,j,j+1)           
tam=30
vec1=[0]*(tam+1)
construyeVector(vec1,16,99)
imprimeVector(vec1,"vector vec1:\t")
ordenaAscen(vec1)
imprimeVector(vec1,"vector vec1 despues de ordenarlo:\t")