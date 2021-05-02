import PySimpleGUI as sg
from src import cantidad
from src import mejores 

def loop():
    layout= [[sg.Button('CANTIDAD DE FUNCIONARIOS' , font=("Helvetica", 19))],
            [sg.Button('LOS 5 MEJORES PAGADOS' , font=("Helvetica", 19))],
            [sg.Button('SALIDA' , font=("Helvetica", 19),button_color=('white', 'red'))]  
    ]
    window = sg.Window("Welcome!", layout, no_titlebar = True , margins=(200,150))
    
    while True:
        event,values = window.read()
        if event == "CANTIDAD DE FUNCIONARIOS" :
            cantidad.start()
        if event == "LOS 5 MEJORES PAGADOS" :
            mejores.start()
        if event == 'SALIDA':
            break
    return window                        


def start():
    window_fun = loop()
    window_fun.close()
    
