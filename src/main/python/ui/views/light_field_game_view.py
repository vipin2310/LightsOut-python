import PySimpleGUI as sg
from ui.views.view import View
from ui.view_manager import ViewManager
from ui.controllers.light_field_game_view_controller import LightFieldGameViewController
from ui.components.light_field_button import LightFieldButton

class LightFieldGameView(View):
    """LightFieldGameView provides the PySimpleGUI Layout for the LightField used to play the game by the user.
    """
    
    def __init__(self) -> None:
        self.num_cols = 5
        self.num_rows = 5
        
        super().__init__()
        
        self.element_padding = (0, 0)
    
    def _create_layout(self) -> list:
        distance_to_window_edge = 50
        
        if ViewManager._width < ViewManager._height:
            length = (ViewManager._width - (2 * distance_to_window_edge) - ((self.num_cols - 1))) // self.num_cols
        else:
            length = (ViewManager._height - (2 * distance_to_window_edge) - ((self.num_rows - 1))) // self.num_rows
        
        button_size = (length, length)
        
        columns = [[[LightFieldButton(light_on=False, size=button_size, key=(x, y))] for y in range(self.num_rows)] for x in range(self.num_cols)]
        
        layout = [[sg.VPush()],
                  [sg.Push()],
                  [sg.VPush()]]
        
        for column in columns:
            layout[1].append(sg.Column(column, element_justification="c", pad=(0,0)))
        layout[1].append(sg.Push())
        
        return layout
    
    def _create_title(self) -> str:
        return "Light Field Game"
    
    def _create_controller(self) -> LightFieldGameViewController:
        return LightFieldGameViewController(self)