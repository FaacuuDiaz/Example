import PySimpleGUI as sg      
from src.constants.session import data
from src.routes.routes import BASE_PATH
def ejecutar():
    layout = [
        [sg.Text('Ventana Primero.')],      
        [sg.B("Data")],      
        [sg.B("Path")],      
        [sg.B("Volver")],      
    ]
    window = sg.Window('Window Title', layout)    


    while True:
        event, values = window.read()    
        if event == "Volver" or event == sg.WIN_CLOSED:
            break
        elif event == "Data":
            print(data)
        elif event == "Path":
            print(BASE_PATH)
    
    window.close()