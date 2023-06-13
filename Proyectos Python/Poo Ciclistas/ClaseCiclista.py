import os
os.system("cls")
import copy

class ciclista():
    def __init__(self,nombre):
        self.nombre=nombre
class tiempo_ciclista(ciclista):
    def __init__(self,nombre=None,num_etapas=None):
        super().__init__(nombre)
        self.etapas=num_etapas
        self.hora=[0]*num_etapas
        self.minuto=[0]*num_etapas
        self.segundo=[0]*num_etapas
        self.etapa_tiempo=[0]*num_etapas
        self.total_tiempo=0
    def tiempo_etapa(self,etapa,horas,minutos,segundos):
        self.hora[etapa-1]=horas
        self.minuto[etapa-1]=minutos
        self.segundo[etapa-1]=segundos
        self.etapa_tiempo[etapa-1]=horas*60+minutos+segundos/60
    def mostrar_tiempo(self,etapa):
        return(f"Etapa N°{etapa}---hora:{self.hora[etapa-1]}--minutos:{self.minuto[etapa-1]}--segundos:{self.segundo[etapa-1]}")
    def tiempo_total(self):
        self.horat=0
        self.minutost=0
        self.segundost=0
        for i in range(0,self.etapas):
            self.segundost+=self.segundo[i]
            if self.segundost>=60:
                self.minutost+=1
                self.segundost=self.segundost-60
            self.minutost+=self.minuto[i]
            if self.minutost>=60:
                self.horat+=1
                self.minutost=self.minutost-60
            self.horat+=self.hora[i]
        self.total_tiempo=self.horat*60+self.minutost+self.segundost/60
        return print("horas:",self.horat,"minutos:",self.minutost,"segundos:",self.segundost)
def ganador_etapa(v,etapa):
    aux=0
    aux=copy.deepcopy(v)
    for i in range(1,aux[0]):
        for j in range(1, aux[0]-i + 1):
            if aux[j].etapa_tiempo[etapa-1]>aux[j+1].etapa_tiempo[etapa-1]:
                intercambiar(aux,j,j+1)
                
    lista_ge=(f"Podio Etapa n°{etapa}",f"Primer  puesto: {aux[1].nombre}",
              f"Segundo puesto: {aux[2].nombre}",f"Tercer  puesto: {aux[3].nombre}")
    return lista_ge
              
def intercambiar(v,a,b):
    aux = v[a]
    v[a] =v[b]
    v[b] =aux

def ganador_carrera(v):
    aux=0
    aux=copy.deepcopy(v)
    for i in range(1,aux[0]):
        for j in range(1, aux[0]-i + 1):
            if aux[j].total_tiempo>aux[j+1].total_tiempo:
                intercambiar(aux,j,j+1)
    lista=["Podio Carrera",
           f"Primer  puesto: {aux[1].nombre}--{aux[1].horat}:{aux[1].minutost}:{aux[1].segundost}",
           f"Segundo puesto: {aux[2].nombre}--{aux[2].horat}:{aux[2].minutost}:{aux[2].segundost}",
           f"Tercer  puesto: {aux[3].nombre}--{aux[3].horat}:{aux[3].minutost}:{aux[3].segundost}"]
    
    return lista
      
