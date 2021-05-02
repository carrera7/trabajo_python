import PySimpleGUI as sg
import funcionarios as fun
import iglesias 

def loop():
    layout= [[sg.Text('¿QUE DATOS DESEA ANALIZAR ?', size=(30, 1), font=("Helvetica", 25), text_color='white')],
            [sg.Button('FUNCIONARIOS' , font=("Helvetica", 20))],
            [sg.Button('IGLESIAS' , font=("Helvetica", 20))],
            [sg.Button('SALIDA' , font=("Helvetica", 20),button_color=('white', 'red'))]  
    ]
    window = sg.Window("Welcome!", layout, no_titlebar = True , margins=(200,150))
    
    while True : 
         event,values = window.read()
         if event == "FUNCIONARIOS" :
             fun.start()
             window.BringToFront()
         if event == "IGLESIAS" :
             iglesias.start()
             window.BringToFront()
         if event == 'SALIDA' or event == sg.WINDOW_CLOSED:
             break
    return window

def start():
    Window_programa = loop()
    Window_programa.close()        