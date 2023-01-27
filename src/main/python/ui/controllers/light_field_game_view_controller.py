import PySimpleGUI as sg
from ui.controllers.controller import Controller
from ui.view_manager import ViewManager
from ui.components.light_field_button import LightFieldButton
from ui.models.light_field_button_grid import LightFieldButtonGrid

class LightFieldGameViewController(Controller):
    """Implements the controller for the LightFieldGameView.
    """
    
    def __init__(self, view, button_grid : LightFieldButtonGrid):
        self.button_grid = button_grid
        
        super().__init__(view)
    
    def handle_event(self, event: str) -> None:
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            ViewManager.terminate()
        elif type(event) == tuple:            
            
            if type(self.view.window[event]) == LightFieldButton:
                self.button_grid.get_button(event).toggle_light()
            
            self.view.read_events()
        else:
            self.view.read_events()
        