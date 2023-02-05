from ui.view_manager import ViewManager
from ui.views.main_menu_view import MainMenuView

if __name__ == "__main__":
    ViewManager.set_view(MainMenuView(), keep_attributes = False)
    ViewManager.set_width(650)
    ViewManager.set_height(700)
    ViewManager.set_min_width(500)
    ViewManager.set_min_height(500)
    ViewManager.set_main_title("Lights Out")
    ViewManager.center_view()
    
    ViewManager.start_event_handler()
    ViewManager.terminate()