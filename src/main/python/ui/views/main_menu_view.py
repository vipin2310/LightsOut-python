import PySimpleGUI as sg
from ui.views.view import View
from ui.controllers.main_menu_view_controller import MainMenuViewController

class MainMenuView(View):
    """MainMenuView provides the functionality to customize the LightField grid and start the game from when player is ready.
    """
    def __init__(self) -> None:
        """
        Creates an instance of this class. It makes the view resizable.
        """
        
        self.row_col_default = 5
        
        super().__init__()
        self.resizable = True
    
    def _create_layout(self) -> list:
        # Docstring see super class
        
        font_header = ("Helvetica", 60, "bold")
        font_button = ("Helvetica", 15)
        button_size = (36, 1)
        
        row_col_input_components = [sg.Text("Number of rows and columns: ", font=font_button), 
                                    sg.Input(self.row_col_default, key="row_col_count", font=font_button, size=(3, 1), enable_events=True), 
                                    sg.Button("↑", key="num_up", size=(2, 1), font=font_button), 
                                    sg.Button("↓", key="num_down", size=(2, 1), font=font_button)]
        
        column = [[sg.Text("Lights out", font=font_header, justification="center")],
                  [sg.Text(size=(12,1))],
                  row_col_input_components,
                  [sg.Button("Play", font=font_button, size=button_size)],
                  [sg.Button("Exit", font=font_button, size=button_size)]]
        
        layout = [[sg.VPush()],
                  [sg.Push(), sg.Column(column, element_justification="c"), sg.Push()],
                  [sg.VPush()]]
        
        return layout
    
    def _create_title(self) -> str:
        # Docstring see super class
        
        return "Main Menu"
    
    def _create_controller(self) -> MainMenuViewController:
        # Docstring see super class
        
        return MainMenuViewController(self, self.row_col_default)
            
        