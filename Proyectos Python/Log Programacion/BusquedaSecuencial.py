import random 
import os
os.system("cls")
"""
Busqueda en un vector con datos desordenados
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
   
def busquedaSec(V,d):
    i=1
    while i<=V[0] and d!=V[i]:
        i=i+1
    if i<=V[0]:
        return i
    return -1    

def agregarDato(d,V,n):
    if esLleno(V,n):
        return
    V[0]=V[0]+1
    V[V[0]]=d
    
def esLleno(V, n):
    if V[0] == n:
        return True
    return False

tam=30
vec1=[0]*(tam+1)
construyeVector(vec1,16,99)
imprimeVector(vec1,"vector vec1:\t")
busqueda=69
encontrar=busquedaSec(vec1,busqueda)
if encontrar==-1:
    print(f"El dato {busqueda} no se encuentra en el vector")
else:
    print(f"El dato {busqueda} se encuentra en la posicion {encontrar} del vector vec1")

 