import PySimpleGUI as sg
from src.ventanas.primero import ejecutar
from src.constants.session import data
def main():
    layout = [
        [sg.Text('My one-shot window.')],      
        [sg.B("Primero")],      
        [sg.B("Segundo")],      
        [sg.B("Tercero")],      
        [sg.B("Cuarto")],      
        [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('Window Title', layout)    

    while True:
        event, values = window.read()    
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        
        if event == "Primero":
            sg.Window.Hide(window)
            ejecutar()
            sg.Window.UnHide(window)
        elif event == "Segundo":
            data['segundo'] = "valor de segunda ventana"
            pass # primero.segundo()
        elif event == "Tercero":
            data['tercero'] = "valor de segunda ventana"
            pass # primero.tercero()
        elif event == "Cuarto":
            data['cuarto'] = "valor de segunda ventana"
            pass # primero.cuarto()

    window.close()