import PySimpleGUI as sg
from ui.controllers.controller import Controller
from ui.view_manager import ViewManager
from ui.components.light_field_button import LightFieldButton
from ui.models.light_model_container import LightModelContainer
from logic.game_logic import GameLogic

class LightFieldGameViewController(Controller):
    """Implements the controller for the LightFieldGameView.
    """
    
    def __init__(self, view, lm_container : LightModelContainer):
        self.lm_container = lm_container
        self.move_count = 0
        
        super().__init__(view)
    
    def handle_event(self, event: str) -> None:
        
        if event == "Finalized":
            GameLogic.set_start_problem(self.lm_container)
        elif event == "Exit" or event == sg.WIN_CLOSED:
            ViewManager.terminate()
        elif type(event) == tuple:            
            
            if type(self.view.window[event]) == LightFieldButton:
                GameLogic.iterate(self.lm_container, event)
                self.move_count += 1
                  
            if GameLogic.is_field_solved(self.lm_container):
                sg.Popup(f"The game is over. You won after {self.move_count} moves.")
            else:
                self.view.read_events()
        else:
            self.view.read_events()
        