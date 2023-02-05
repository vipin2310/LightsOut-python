import PySimpleGUI as sg
from ui.views.view import View
from ui.view_manager import ViewManager
from ui.controllers.light_field_game_view_controller import LightFieldGameViewController
from ui.models.light_model_container import LightModelContainer

class LightFieldGameView(View):
    """LightFieldGameView provides the PySimpleGUI Layout for the LightField used to play the game by the user.
    """
    
    def __init__(self, num_cols : int, num_rows : int) -> None:       
        distance_to_window_edge = 50
        if ViewManager._width < ViewManager._height:
            length = (ViewManager._width - (2 * distance_to_window_edge) - ((num_cols - 1))) // num_cols
        else:
            length = (ViewManager._height - (2 * distance_to_window_edge) - ((num_rows - 1))) // num_rows
        button_size = (length, length)
        
        self._lm_container = LightModelContainer(button_size, num_rows, num_cols)
        
        super().__init__()
    
    def _create_layout(self) -> list:
        font = ("Helvetica", 12)
        font_moves = ("Helvetica", 14, "bold")
        layout = [[sg.VPush()],
                  [sg.Push(), sg.Text("Moves: XX", key="MOVE_COUNT_TEXT", pad=(1,10), font=font_moves), sg.Push()],
                  [sg.Push()] + self._lm_container.get_layout_for_view() + [sg.Push()],
                  [sg.Push(), sg.Button("Back to menu", pad=(2,10), font=font), sg.Button("Reset", pad=(2,10), font=font), sg.Push()],
                  [sg.VPush()]]
        
        return layout
    
    def _create_title(self) -> str:
        return "Light Field Game"
    
    def _create_controller(self) -> LightFieldGameViewController:
        return LightFieldGameViewController(self, self._lm_container)
    
    def _finalized(self) -> None:
        self.controller.handle_event("Finalized", None)