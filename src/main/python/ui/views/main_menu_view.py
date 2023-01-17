import PySimpleGUI as sg
from ui.views.view import View
from ui.controllers.main_menu_view_controller import MainMenuViewController

class MainMenuView(View):
    """MainMenuView provides the PySimpleGUI Layout for the Main Menu for this game.
    """
    def __init__(self) -> None:
        super().__init__()
        
        self.resizable = True
    
    def _create_layout(self) -> list:
        font_header = ("Helvetica", 60, "bold")
        font_button = ("Helvetica", 15)
        button_size = (35, 1)
        
        column = [[sg.Text("Lights out", font=font_header, justification="center")],
                  [sg.Text(size=(12,1))],
                  [sg.Button("Standard mode", font=font_button, size=button_size)], 
                  [sg.Button("Exit", font=font_button, size=button_size)]]
        
        layout = [[sg.VPush()],
                  [sg.Push(), sg.Column(column, element_justification="c"), sg.Push()],
                  [sg.VPush()]]
        
        return layout
    
    def _create_title(self) -> str:
        return "Main Menu"
    
    def _create_controller(self) -> MainMenuViewController:
        return MainMenuViewController(self)
            
        