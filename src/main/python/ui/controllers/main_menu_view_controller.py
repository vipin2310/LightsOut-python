import PySimpleGUI as sg
from ui.controllers.controller import Controller
from ui.view_manager import ViewManager
from ui.views.light_field_game_view import LightFieldGameView

class MainMenuViewController(Controller):
    """Implements the controller for the MainMenuView.
    """
    def __init__(self, view, row_col_default : int):
        self.row_col_key = "row_col_count"      
        self.saved_values = {self.row_col_key : row_col_default}
        
        
        super().__init__(view)
    
    def handle_event(self, event : str, values : dict) -> None:
        
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
        valid_value = min(max(1, row_col_count), 20)
        self.saved_values[self.row_col_key] = valid_value
        self.view.window[self.row_col_key].update(valid_value)
    
    def is_int(self, arg) -> bool:
        try: 
            int(arg)
        except ValueError:
            return False
        else:
            return True
        