import PySimpleGUI as sg
from src import cantidad2
from src import grandes 

def loop():
    
    layout= [[sg.Button('CANTIDAD DE IGLESIAS' , font=("Helvetica", 19))],
            [sg.Button('LAS 5 IGLESIAS MAS GRANDES' , font=("Helvetica", 19))],
            [sg.Button('SALIDA' , font=("Helvetica", 19) , button_color=('white', 'red'))]  
    ]
    window = sg.Window("Welcome!", layout, no_titlebar = True , margins=(200,150))

    while True:
        event,values = window.read()
        if event == "CANTIDAD DE IGLESIAS":
            cantidad2.start()
        if event == "LAS 5 IGLESIAS MAS GRANDES":
            grandes.start()
        if event == 'SALIDA':
            break
    return window                        


def start():
    window_igle = loop()
    window_igle.close()