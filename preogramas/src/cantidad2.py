import csv
import json
import PySimpleGUI as sg

def cantidad(csvreader):
    cant = 0 
    for linea in csvreader:
         cant = cant + 1
    cant = cant - 1     
    sg.Popup("La cantidad de iglesias en Buenos Aires es  ", cant)
    
    archivo=open("cantidad-de-iglecias.json", "w")
    dato = [{"cantidad-de-iglesias" : cant }]
    json.dump(dato,archivo,indent=2)
    archivo.close()

def start():
    archivo = open("iglesias.csv", "r")
    csvreader = csv.reader(archivo,delimiter=",")
    inicio = cantidad(csvreader)
    archivo.close()  