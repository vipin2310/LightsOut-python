import PySimpleGUI as sg
from ui.views.view import View
from ui.view_manager import ViewManager
from ui.controllers.light_field_game_view_controller import LightFieldGameViewController
from ui.models.light_model_container import LightModelContainer

class LightFieldGameView(View):
    """LightFieldGameView provides the PySimpleGUI Layout for the LightField used to play the game by the user.
    """
    
    def __init__(self) -> None:
        num_cols = 5
        num_rows = 5
        
        distance_to_window_edge = 50
        if ViewManager._width < ViewManager._height:
            length = (ViewManager._width - (2 * distance_to_window_edge) - ((num_cols - 1))) // num_cols
        else:
            length = (ViewManager._height - (2 * distance_to_window_edge) - ((num_rows - 1))) // num_rows
        button_size = (length, length)
        
        self._lm_container = LightModelContainer(button_size, num_rows, num_cols)
        
        super().__init__()
    
    def _create_layout(self) -> list:        
        layout = [[sg.VPush()],
                  [sg.Push()] + self._lm_container.get_layout_for_view() + [sg.Push()],
                  [sg.VPush()]]
        
        return layout
    
    def _create_title(self) -> str:
        return "Light Field Game"
    
    def _create_controller(self) -> LightFieldGameViewController:
        return LightFieldGameViewController(self, self._lm_container)