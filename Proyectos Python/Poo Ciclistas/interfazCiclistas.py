import tkinter as tk
import tkinter.font as tkFont
from typing import Sized
from ClaseCiclista import ciclista, ganador_etapa,tiempo_ciclista,ganador_carrera
from tkinter import Listbox, messagebox as alerta


class App():
    def __init__(self, root):
        #setting title
        root.title("Vuelta Colombia")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.configure(bg="DarkOliveGreen1")
        root.resizable(width=False, height=False)
        
        self.radioValue =tk.IntVar()

        GLabel_877=tk.Label(root)
        GLabel_877["activeforeground"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=26)
        GLabel_877["font"] = ft
        GLabel_877["fg"] = "#333333"
        GLabel_877["justify"] = "center"
        GLabel_877["text"] = "Vuelta Colombia"
        GLabel_877["bg"] = "DarkOliveGreen1"
        GLabel_877.place(x=170,y=20,width=272,height=76)

        GLabel_950=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_950["font"] = ft
        GLabel_950["fg"] = "#333333"
        GLabel_950["justify"] = "center"
        GLabel_950["text"] = "Ingrese el nombre del ciclista"
        GLabel_950["bg"] = "DarkOliveGreen1"
        GLabel_950.place(x=20,y=190,width=169,height=30)

        self.nombre=tk.Entry(root)
        self.nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nombre["font"] = ft
        self.nombre["fg"] = "#333333"
        self.nombre["justify"] = "center"
        self.nombre["text"] = "Nombre"
        self.nombre["bg"] = "LightYellow2"
        self.nombre.place(x=250,y=190,width=288,height=30)
        

        GLabel_318=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_318["font"] = ft
        GLabel_318["fg"] = "#333333"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "Etapas"
        GLabel_318["bg"] = "DarkOliveGreen1"
        GLabel_318.place(x=0,y=110,width=300,height=30)

        self.tiempo_1L=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        self.tiempo_1L["font"] = ft
        self.tiempo_1L["fg"] = "#333333"
        self.tiempo_1L["justify"] = "center"
        self.tiempo_1L["text"] = "Tiempo etapa N°1"
        self.tiempo_1L["bg"] = "DarkOliveGreen1"
        self.tiempo_1L.place(x=0,y=270,width=171,height=30)
        self.tiempo_1L.place_forget()

        self.tiempo_1=tk.Entry(root)
        self.tiempo_1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.tiempo_1["font"] = ft
        self.tiempo_1["fg"] = "#333333"
        self.tiempo_1["justify"] = "center"
        self.tiempo_1["text"] = "Tiempo 1"
        self.tiempo_1.place(x=200,y=270,width=119,height=30)
        self.tiempo_1["bg"] = "LightYellow2"
        self.tiempo_1.place_forget()

        self.guardar=tk.Button(root)
        self.guardar["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.guardar["font"] = ft
        self.guardar["fg"] = "#000000"
        self.guardar["justify"] = "center"
        self.guardar["text"] = "guardar"
        self.guardar.place(x=460,y=280,width=96,height=32)
        self.guardar["bg"] = "LightYellow2"
        self.guardar["command"] = self.GButton_411_command

        self.etapa1=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        self.etapa1["font"] = ft
        self.etapa1["fg"] = "#333333"
        self.etapa1["justify"] = "center"
        self.etapa1["text"] = "1 Etapa"
        self.etapa1.place(x=210,y=110,width=85,height=25)
        self.etapa1["variable"] =self.radioValue
        self.etapa1["value"]=1
        self.etapa1["bg"] = "DarkOliveGreen1"
        self.etapa1["command"] = self.Getapa1

        self.etapa2=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        self.etapa2["font"] = ft
        self.etapa2["fg"] = "#333333"
        self.etapa2["justify"] = "center"
        self.etapa2["text"] = "2 Etapas"
        self.etapa2.place(x=300,y=110,width=85,height=25)
        self.etapa2["variable"] =self.radioValue
        self.etapa2["value"]=2
        self.etapa2["bg"] = "DarkOliveGreen1"
        self.etapa2["command"] = self.Getapa2

        self.etapa3=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        self.etapa3["font"] = ft
        self.etapa3["fg"] = "#333333"
        self.etapa3["justify"] = "center"
        self.etapa3["text"] = "3 Etapas"
        self.etapa3.place(x=380,y=110,width=85,height=25)
        self.etapa3["variable"] =self.radioValue
        self.etapa3["value"]=3
        self.etapa3["bg"] = "DarkOliveGreen1"
        self.etapa3["command"] = self.Getapa3

        self.tiempo_2L=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        self.tiempo_2L["font"] = ft
        self.tiempo_2L["fg"] = "#333333"
        self.tiempo_2L["justify"] = "center"
        self.tiempo_2L["text"] = "Tiempo etapa N°2"
        self.tiempo_2L.place(x=10,y=330,width=150,height=30)
        self.tiempo_2L["bg"] = "DarkOliveGreen1"
        self.tiempo_2L.place_forget()

        self.tiempo_3L=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        self.tiempo_3L["font"] = ft
        self.tiempo_3L["fg"] = "#333333"
        self.tiempo_3L["justify"] = "center"
        self.tiempo_3L["text"] = "Tiempo etapa N°3"
        self.tiempo_3L.place(x=20,y=390,width=133,height=30)
        self.tiempo_3L["bg"] = "DarkOliveGreen1"
        self.tiempo_3L.place_forget()

        self.tiempo_2=tk.Entry(root)
        self.tiempo_2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.tiempo_2["font"] = ft
        self.tiempo_2["fg"] = "#333333"
        self.tiempo_2["justify"] = "center"
        self.tiempo_2["text"] = "Tiempo 2"
        self.tiempo_2.place(x=200,y=330,width=119,height=30)
        self.tiempo_2["bg"] = "LightYellow2"
        self.tiempo_2.place_forget()

        self.tiempo_3=tk.Entry(root)
        self.tiempo_3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.tiempo_3["font"] = ft
        self.tiempo_3["fg"] = "#333333"
        self.tiempo_3["justify"] = "center"
        self.tiempo_3["text"] = "Tiempo 3"
        self.tiempo_3.place(x=200,y=390,width=122,height=30)
        self.tiempo_3["bg"] = "LightYellow2"
        self.tiempo_3.place_forget()
        
        self.nb=tk.Button(root)
        self.nb["bg"] = "tan1"
        ft = tkFont.Font(family='Times',size=10)
        self.nb["font"] = ft
        self.nb["fg"] = "#000000"
        self.nb["justify"] = "center"
        self.nb["text"] = "Ganadores"
        self.nb["bg"] = "LightYellow2"
        self.nb.place(x=460,y=350,width=96,height=32)
        self.nb.place_forget()
        self.nb["command"] = self.createNewWindow
        
        GLabel_90=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_90["font"] = ft
        GLabel_90["fg"] = "#333333"
        GLabel_90["justify"] = "center"
        GLabel_90["bg"] = "DarkOliveGreen1"
        GLabel_90["text"] = "Ingrese solo tres ciclistas"
        GLabel_90.place(x=175,y=150,width=249,height=30)
        
        self.anuncio=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.anuncio["font"] = ft
        self.anuncio["fg"] = "#333333"
        self.anuncio["justify"] = "center"
        self.anuncio["text"] = "Hora:Minuto:Segundo"
        self.anuncio["bg"] = "DarkOliveGreen1"
        self.anuncio.place(x=200,y=230,width=120,height=30)
        self.anuncio.place_forget()
        
        quit=tk.Button(text="SALIR", fg="black",font=ft, command=root.destroy).place(x=235,y=450,width=125,height=32)


        self.i=1
        self.v=[0]*4
        self.v[0]=3
    def GButton_411_command(self):
        try:
            self.v[self.i]=tiempo_ciclista(self.nombre.get(),self.eta)
            if self.eta==1:
                hora,minutos,segundos=self.tiempo_1.get().split(":")
                self.v[self.i].tiempo_etapa(1,int(hora),int(minutos),int(segundos))
                self.v[self.i].tiempo_total()
            elif self.eta==2:
                hora,minutos,segundos=self.tiempo_1.get().split(":")
                self.v[self.i].tiempo_etapa(1,int(hora),int(minutos),int(segundos))
                hora,minutos,segundos=self.tiempo_2.get().split(":")
                self.v[self.i].tiempo_etapa(2,int(hora),int(minutos),int(segundos))
                self.v[self.i].tiempo_total()
            elif self.eta==3:
                hora,minutos,segundos=self.tiempo_1.get().split(":")
                self.v[self.i].tiempo_etapa(1,int(hora),int(minutos),int(segundos))
                hora,minutos,segundos=self.tiempo_2.get().split(":")
                self.v[self.i].tiempo_etapa(2,int(hora),int(minutos),int(segundos))
                hora,minutos,segundos=self.tiempo_3.get().split(":")
                self.v[self.i].tiempo_etapa(3,int(hora),int(minutos),int(segundos))
                self.v[self.i].tiempo_total()
            print(self.v[self.i].hora)
            print(self.v[self.i].minuto)
            print(self.v[self.i].segundo)
                 
        except :
            alerta.showerror("CORRECCIÓN","Solo se permiten 3")
        
        self.nombre.delete(0,"end")
        self.tiempo_1.delete(0,"end")
        self.tiempo_2.delete(0,"end")
        self.tiempo_3.delete(0,"end")
        if (self.i)==3:
            self.nb.place(x=460,y=350,width=96,height=32)
        self.i+=1    
         

    def Getapa1(self):
        self.etapa2.place_forget()
        self.etapa3.place_forget()
        self.eta=self.radioValue.get()
        self.tiempo_1L.place(x=0,y=270,width=171,height=30)
        self.tiempo_1.place(x=200,y=270,width=119,height=30)
        self.anuncio.place(x=200,y=230,width=120,height=30)


    def Getapa2(self):
        self.etapa1.place_forget()
        self.etapa3.place_forget()
        self.eta=self.radioValue.get()
        self.tiempo_1L.place(x=0,y=270,width=171,height=30)
        self.tiempo_1.place(x=200,y=270,width=119,height=30)
        self.tiempo_2L.place(x=10,y=330,width=150,height=30)
        self.tiempo_2.place(x=200,y=330,width=119,height=30)
        self.anuncio.place(x=200,y=230,width=120,height=30)


    def Getapa3(self):
        self.etapa1.place_forget()
        self.etapa2.place_forget()
        self.eta=self.radioValue.get()
        self.tiempo_1L.place(x=0,y=270,width=171,height=30)
        self.tiempo_1.place(x=200,y=270,width=119,height=30)
        self.tiempo_2L.place(x=10,y=330,width=150,height=30)
        self.tiempo_2.place(x=200,y=330,width=119,height=30)
        self.tiempo_3L.place(x=20,y=390,width=133,height=30)
        self.tiempo_3.place(x=200,y=390,width=122,height=30)
        self.anuncio.place(x=200,y=230,width=120,height=30)
        
    def createNewWindow(self):
        newWindow = tk.Toplevel(root)
        width=400
        height=300
        screenwidth = newWindow.winfo_screenwidth()
        screenheight = newWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        newWindow.geometry(alignstr)
        newWindow.configure(bg="DarkOliveGreen1")
        newWindow.resizable(width=False, height=False)
        
        self.radioValue_nw=tk.IntVar()
        
        self.GRadio_592=tk.Radiobutton(newWindow)
        ft = tkFont.Font(family='Times',size=10)
        self.GRadio_592["font"] = ft
        self.GRadio_592["fg"] = "#333333"
        self.GRadio_592["justify"] = "center"
        self.GRadio_592["text"] = "1 etapa"
        self.GRadio_592.place(x=130,y=30,width=85,height=25)
        self.GRadio_592["bg"] = "DarkOliveGreen1"
        self.GRadio_592["variable"] =self.radioValue_nw
        self.GRadio_592["value"]=1
        self.GRadio_592["command"] = self.GRadio_592_command

        self.GRadio_871=tk.Radiobutton(newWindow)
        ft = tkFont.Font(family='Times',size=10)
        self.GRadio_871["font"] = ft
        self.GRadio_871["fg"] = "#333333"
        self.GRadio_871["justify"] = "center"
        self.GRadio_871["text"] = "2 etapa"
        self.GRadio_871.place(x=210,y=30,width=85,height=25)
        self.GRadio_871["bg"] = "DarkOliveGreen1"
        self.GRadio_871["variable"] =self.radioValue_nw
        self.GRadio_871["value"]=2
        self.GRadio_871["command"] = self.GRadio_871_command

        self.GRadio_526=tk.Radiobutton(newWindow)
        ft = tkFont.Font(family='Times',size=10)
        self.GRadio_526["font"] = ft
        self.GRadio_526["fg"] = "#333333"
        self.GRadio_526["justify"] = "center"
        self.GRadio_526["text"] = "3 etapa"
        self.GRadio_526.place(x=290,y=30,width=85,height=25)
        self.GRadio_526["bg"] = "DarkOliveGreen1"
        self.GRadio_526["variable"] =self.radioValue_nw
        self.GRadio_526["value"]=3
        self.GRadio_526["command"] = self.GRadio_526_command
        
        if self.eta==1:
            self.GRadio_871.place_forget()
            self.GRadio_526.place_forget()
        elif self.eta==2:
            self.GRadio_526.place_forget()
            
        self.GLabel_949=tk.Label(newWindow)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_949["font"] = ft
        self.GLabel_949["fg"] = "#333333"
        self.GLabel_949["justify"] = "center"
        self.GLabel_949["text"] = "Ganador por etapa"
        self.GLabel_949["bg"] = "DarkOliveGreen1"
        self.GLabel_949.place(x=0,y=30,width=117,height=30)

        self.GListBox_560=tk.Listbox(newWindow)
        self.GListBox_560["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GListBox_560["font"] = ft
        self.GListBox_560["fg"] = "#333333"
        self.GListBox_560["justify"] = "center"
        self.GListBox_560["bg"] = "DarkOliveGreen1"
        self.GListBox_560.place(x=150,y=80,width=206,height=74)
        
        GLabel_16=tk.Label(newWindow)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_16["font"] = ft
        GLabel_16["fg"] = "#333333"
        GLabel_16["justify"] = "center"
        GLabel_16["text"] = "Ganador de la carrea"
        GLabel_16["bg"] = "DarkOliveGreen1"
        GLabel_16.place(x=120,y=160,width=161,height=30)

        self.GListBox_592=tk.Listbox(newWindow)
        self.GListBox_592["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GListBox_592["font"] = ft
        self.GListBox_592["fg"] = "#333333"
        self.GListBox_592["justify"] = "center"
        self.GListBox_592["bg"] = "DarkOliveGreen1"
        self.GListBox_592.place(x=110,y=220,width=183,height=72)
        
        GButton_666=tk.Button(newWindow)
        GButton_666["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_666["font"] = ft
        GButton_666["fg"] = "#000000"
        GButton_666["justify"] = "center"
        GButton_666["text"] = "Ver Ganador"
        GButton_666["bg"] = "DarkOliveGreen1"
        GButton_666.place(x=170,y=190,width=77,height=30)
        GButton_666["command"] = self.GButton_666_command

    def GRadio_592_command(self):
        self.GListBox_560.delete(0, tk.END)
        self.eta_nw=self.radioValue_nw.get()
        self.GListBox_560.insert(0,*ganador_etapa(self.v,self.eta_nw))
        
    def GRadio_871_command(self):
        self.GListBox_560.delete(0, tk.END)
        self.eta_nw=self.radioValue_nw.get()
        self.GListBox_560.insert(0,*ganador_etapa(self.v,self.eta_nw))

    def GRadio_526_command(self):
        self.GListBox_560.delete(0, tk.END)
        self.eta_nw=self.radioValue_nw.get()
        self.GListBox_560.insert(0,*ganador_etapa(self.v,self.eta_nw))

    def GButton_666_command(self):
        self.GListBox_592.insert(0,*ganador_carrera(self.v))
    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


