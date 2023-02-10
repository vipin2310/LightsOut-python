import PySimpleGUI as sg
from ui.controllers.controller import Controller
from ui.view_manager import ViewManager
from ui.components.light_field_button import LightFieldButton
from ui.models.light_model_container import LightModelContainer
from logic.game_logic import GameLogic
import ui.views.main_menu_view

class LightFieldGameViewController(Controller):
    """Implements the controller for the LightFieldGameView.
    """
    
    def __init__(self, view, lm_container : LightModelContainer):
        """
        Creates an instance of a controller for the LightFieldGameView.

        Parameters
        ----------
        view : View
            The view that will be controlled (according to MVC)
        lm_container : LightModelContainer
            The LightModelContainer which the game logic will operate on.
        """
        self.lm_container = lm_container
        self.move_count = 0
        
        super().__init__(view)
    
    def handle_event(self, event : str, values : dict) -> None:
        # Docstring see super class
        
        if event == "Finalized":
            GameLogic.set_new_start_problem(self.lm_container)
            self.update_move_count_text()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            ViewManager.terminate()
        elif event == "Reset":
            GameLogic.reset_start_problem(self.lm_container)
            self.move_count = 0
            self.update_move_count_text()
            self.view.read_events()
        elif event == "Back to menu":
            self._show_main_menu()
        elif type(event) == tuple:
            
            if type(self.view.window[event]) == LightFieldButton:
                GameLogic.iterate(self.lm_container, event)
                self.move_count += 1
                self.update_move_count_text()
                  
            if GameLogic.is_field_solved(self.lm_container):
                self.show_success_popup()
            else:
                self.view.read_events()
        else:
            self.view.read_events()

    def show_success_popup(self):
        """
        Displays the popup for successfully solving the LightFieldGame.
        """
        
        font = ("Helvetica", 12)
        win_msg = f"You won after {self.move_count} move." if self.move_count == 1 else f"You won after {self.move_count} moves."
        
        popup_event, values = sg.Window("Lights Out!",
                                         [[sg.Text("Lights Out! The game is over.", font=font)], 
                                          [sg.Text(win_msg, font=font)],
                                          [sg.Button("Restart", font=font), sg.Button("Exit", font=font)]], 
                                         element_justification='c', keep_on_top=True, size=(300,100)).read(close=True)
                
        if popup_event == "Exit" or popup_event == sg.WIN_CLOSED:
            ViewManager.terminate()
        else:
            self._show_main_menu()
    
    def update_move_count_text(self) -> None:
        """
        Updates the move count text in the GUI.
        """
        
        self.view.window["MOVE_COUNT_TEXT"].update(f"Moves: {self.move_count}")
        
    def _show_main_menu(self):
        """
        Function that returns to the main menu.
        """
        
        ViewManager.set_view(ui.views.main_menu_view.MainMenuView())
        ViewManager.center_view()
        ViewManager.start_event_handler()