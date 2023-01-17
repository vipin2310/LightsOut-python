import PySimpleGUI as sg
from ui.controllers.controller import Controller
from ui.view_manager import ViewManager
from ui.components.light_field_button import LightFieldButton

class LightFieldGameViewController(Controller):
    """Implements the controller for the LightFieldGameView.
    """
    
    def handle_event(self, event: str) -> None:
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            ViewManager.terminate()
        elif type(event) == tuple:
            element = self.view.window[event]
            
            if type(element) == LightFieldButton:
                element.toggle_light_on()
            
            self.view.read_events()
        else:
            self.view.read_events()
        