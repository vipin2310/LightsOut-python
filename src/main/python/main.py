from ui.view_manager import ViewManager
from ui.views.main_menu_view import MainMenuView

if __name__ == "__main__":
    manager = ViewManager.get_instance()
    manager.set_view(MainMenuView())
    manager.set_width(650)
    manager.set_height(650)
    manager.set_min_width(500)
    manager.set_min_height(500)
    manager.set_main_title("Lights out")
    
    manager.start_event_handler()
    manager.terminate()