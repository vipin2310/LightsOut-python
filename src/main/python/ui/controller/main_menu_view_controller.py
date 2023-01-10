import PySimpleGUI as sg
from ui.controller.controller import Controller
from ui.view_manager import ViewManager

class MainMenuViewController(Controller):
    """Implements the controller for the MainMenuView.
    """
    
    def handle_event(self, event: str) -> None:
        manager = ViewManager.get_instance()
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            manager.terminate()
        elif event == "Standard mode":
            self.view.read_events()
        