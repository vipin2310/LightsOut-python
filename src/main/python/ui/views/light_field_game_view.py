import PySimpleGUI as sg
from ui.views.view import View
from ui.view_manager import ViewManager
from ui.controllers.light_field_game_view_controller import LightFieldGameViewController
from ui.models.light_model_container import LightModelContainer

class LightFieldGameView(View):
    """LightFieldGameView provides the LightField and controls used to play the game by the player.
    """
    
    def __init__(self, num_cols : int, num_rows : int) -> None:
        """
        Creates an instance of the LightFieldGameView which displays the LightField grid the 
        player can interact to play the game.

        Parameters
        ----------
        num_cols : int
            Number of columns for the LightField.
        num_rows : int
            Number of rows for the LightField.
        """

        button_size = self.calculate_button_size(num_cols, num_rows)
        self._lm_container = LightModelContainer(button_size, num_rows, num_cols)
        
        super().__init__()

    def calculate_button_size(self, num_cols : int, num_rows : int, distance_to_window_edge : int = 50) -> tuple[int, int]:
        """
        Calculates the button sizes for the grid which will be used for the LightField.

        Parameters
        ----------
        num_cols : int
            Number of columns.
        num_rows : int
            Number of rows.
        distance_to_window_edge : int, optional
            Distance of the LightField to window edges (no exactly given in pixels), by default 50

        Returns
        -------
        button_size : tuple[int, int]
            The button sizes for the LightFieldButtons.
        """
        
        if ViewManager._width < ViewManager._height:
            length = (ViewManager._width - (2 * distance_to_window_edge) - (num_cols - 1)) // num_cols
        else:
            length = (ViewManager._height - (2 * distance_to_window_edge) - (num_rows - 1)) // num_rows
        button_size = (length, length)
        
        return button_size
    
    def _create_layout(self) -> list:
        # For docstring see super class
        
        font = ("Helvetica", 12)
        font_moves = ("Helvetica", 14, "bold")
        layout = [[sg.VPush()],
                  [sg.Push(), sg.Text("Click the light buttons to switch the lights on or off. You will succeed after all lights are off.", font=font), sg.Push()],
                  [sg.Push(), sg.Text("Moves: XX", key="MOVE_COUNT_TEXT", pad=(1,15), font=font_moves), sg.Push()],
                  [sg.Push()] + self._lm_container.get_layout_for_view() + [sg.Push()],
                  [sg.Push(), sg.Button("Back to menu", pad=(5,15), font=font), sg.Button("Reset", pad=(5,15), font=font), sg.Push()],
                  [sg.VPush()]]
        
        return layout
    
    def _create_title(self) -> str:
        # For docstring see super class
        
        return "Light Field Game"
    
    def _create_controller(self) -> LightFieldGameViewController:
        # For docstring see super class
        
        return LightFieldGameViewController(self, self._lm_container)
    
    def _finalized(self) -> None:
        # For docstring see super class
        
        self.controller.handle_event("Finalized", None)