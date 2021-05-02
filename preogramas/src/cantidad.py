import csv
import json
import PySimpleGUI as sg

def cantidad (csvreader):
    cant = 0 
    for linea in csvreader:
        cant = cant + 1
    cant = cant-1    
    sg.Popup(" La cantidad de funcionarios es", cant)
    
    archivo=open("cantidad-de-funcionarios.json", "w")
    dato = [{"cantidad-de-funcionarios" : cant }]
    json.dump(dato,archivo,indent=2)
    archivo.close()

def start():
    archivo = open( "SUELDOs_FUNCIONARIOS_2021.csv" , "r")
    csvreader= csv.reader(archivo,delimiter = ",")
    inicio = cantidad(csvreader)
    archivo.close()  