import PySimpleGUI as sg
from ui.controllers.controller import Controller
from ui.view_manager import ViewManager
from ui.components.light_field_button import LightFieldButton
from ui.models.light_model_container import LightModelContainer

class LightFieldGameViewController(Controller):
    """Implements the controller for the LightFieldGameView.
    """
    
    def __init__(self, view, lm_container : LightModelContainer):
        self.lm_container = lm_container
        
        super().__init__(view)
    
    def handle_event(self, event: str) -> None:
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            ViewManager.terminate()
        elif type(event) == tuple:            
            
            if type(self.view.window[event]) == LightFieldButton:
                self.lm_container.get_light_model(event).toggle_light_on()    
                neighbors = self.lm_container.get_neighbors(event)
            
                # Using map function to replace for-loop
                neighbors[:] = map(lambda lm : lm.toggle_light_on() if lm != None else lm, neighbors)
            
            self.view.read_events()
        else:
            self.view.read_events()
        