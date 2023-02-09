import PySimpleGUI as sg
from ui.controllers.controller import Controller
from ui.view_manager import ViewManager
from ui.views.light_field_game_view import LightFieldGameView

class MainMenuViewController(Controller):
    """Implements the controller for the MainMenuView.
    """
    
    def __init__(self, view, row_col_default : int):
        """
        Creates an instance of a controller for the MainMenuView.

        Parameters
        ----------
        view : View
            The MainMenuView which will be controlled (according to MVC).
        row_col_default : int
            The default value for the rows and columns in the grid, which can be edited by the user.
        """
        self.row_col_key = "row_col_count"      
        self.saved_values = {self.row_col_key : row_col_default}
        
        
        super().__init__(view)
    
    def handle_event(self, event : str, values : dict) -> None:
        # For docstring see super class
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            ViewManager.terminate()
        elif event == self.row_col_key:
            element, text = self.view.window[self.row_col_key], values[self.row_col_key]
            
            if not self.is_int(text):
                element.update(self.saved_values[self.row_col_key])
            elif int(text) != self.saved_values[self.row_col_key]:
                self.update_row_col_count(int(text))
                
            self.view.read_events()
        elif event == "num_up":
            element, text = self.view.window[self.row_col_key], values[self.row_col_key]
            
            if not self.is_int(text):
                element.update(self.saved_values[self.row_col_key])
            else:
                self.update_row_col_count(int(text) + 1)
            self.view.read_events()
        elif event == "num_down":
            element, text = self.view.window[self.row_col_key], values[self.row_col_key]
            
            if not self.is_int(text):
                element.update(self.saved_values[self.row_col_key])
            else:
                self.update_row_col_count(int(text) - 1)
            self.view.read_events()
        elif event == "Play":
            row_col_value = self.saved_values[self.row_col_key]
            ViewManager.set_view(LightFieldGameView(row_col_value, row_col_value))
            ViewManager.center_view()
            ViewManager.start_event_handler()
    
    def update_row_col_count(self, row_col_count : int) -> None:
        """
        Updates the row / column count value in the MainMenuView with a valid value (between 1 and 20).

        Parameters
        ----------
        row_col_count : int
            The value which should be set.
            (Will be checked if valid and if not, a valid value will be used instead)
        """
        
        valid_value = min(max(1, row_col_count), 20)
        self.saved_values[self.row_col_key] = valid_value
        self.view.window[self.row_col_key].update(valid_value)
    
    def is_int(self, arg) -> bool:
        """
        Checks if the argument is an integer or not.

        Parameters
        ----------
        arg : Any
            The argument which will be checked if it is integer

        Returns
        -------
        bool
            True if it is integer, else false.
        """
        try: 
            int(arg)
        except ValueError:
            return False
        else:
            return True
        