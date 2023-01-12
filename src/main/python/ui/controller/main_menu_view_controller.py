import PySimpleGUI as sg
from ui.controller.controller import Controller
from ui.view_manager import ViewManager
from ui.views.light_field_game_view import LightFieldGameView

class MainMenuViewController(Controller):
    """Implements the controller for the MainMenuView.
    """
    
    def handle_event(self, event: str) -> None:
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            ViewManager.terminate()
        elif event == "Standard mode":
            ViewManager.set_view(LightFieldGameView())
            ViewManager.start_event_handler()
        