import csv
import json
import PySimpleGUI as sg

def mejores_5(csvreader):
    
 lista = [["null",0],["null",0],["null",0],["null",0],["null",0]]
 i = 0
 completo = True
 pasa = True
 for linea in csvreader:
        if(not pasa):
            if(completo):
                 lista[i][0]=linea[2]
                 num = int(linea[4])
                 lista[i][1]= num  
                 i = i+1
                 if(i > 4):
                     completo = False
            else:
                 j=0
                 ok = True
                 while j < 5 and ok:
                         if(lista[j][1] < int(linea[4])):
                             lista[j][0]=linea[2]
                             lista[j][1]=int(linea[4])
                             ok = False
                         j = j+1
        else:
             pasa = False
 return(lista)

def convertir(lista):
    archivo = open("iglesias.json","w")
    datos =[{"nombre":lista[0][0] , "dimencion":lista[0][1]},{"nombre":lista[1][0] , "dimencion":lista[1][1]},
    {"nombre":lista[2][0] , "dimencion":lista[2][1]},{"nombre":lista[3][0] , "dimencion":lista[3][1]},
    {"nombre":lista[4][0] , "dimencion":lista[4][1]}]
    json.dump(datos,archivo,indent=2)
    archivo.close() 

def loop(csvreader):
    
    lista = mejores_5(csvreader)     
    convertir(lista)
    layout = [[sg.Text("Estos son las 5 iglesias mas grandes  " , font=("Helvetica", 25))],
             [sg.Listbox(lista,font=("Helvetica", 15),size=(60, 6))],
             [sg.Button('SALIDA' , font=("Helvetica", 12))] 
        ]
    window = sg.Window("Welcome!", layout, no_titlebar = True  , margins=(200,150))
    event,values = window.read()
    if  event == "SALIDA" or event == sg.WINDOW_CLOSED:
        window.close()         
    window.close()

def start():
    archivo = open("iglesias.csv", "r")
    csvreader = csv.reader(archivo,delimiter=",") 
    inicio = loop(csvreader)
    archivo.close()    