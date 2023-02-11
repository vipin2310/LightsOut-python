from ui.view_manager import ViewManager
from ui.views.main_menu_view import MainMenuView

if __name__ == "__main__":
    """
    Entry point for the game project LIGHTSOUT-PYTHON! Use this to launch the game.
    
    Sets the MainMenuView per default with fixed properties (width, height, etc.).
    """
    # Initializing the MainMenuView and its properties
    ViewManager.set_view(MainMenuView(), keep_attributes = False)
    ViewManager.set_width(650)
    ViewManager.set_height(750)
    ViewManager.set_min_width(500)
    ViewManager.set_min_height(500)
    ViewManager.set_main_title("Lights Out")
    ViewManager.center_view()
    
    # Starting event handling
    ViewManager.start_event_handler()
    
    # Ensure termination after everything finished
    ViewManager.terminate()