import PySimpleGUI
from views import View
from typing import Self

class ViewManager:
    """Manages the views for the game. This class follows the Singleton pattern.
    """
    
    def get_instance() -> Self:
        """Returns a single instance of this class.

        Returns:
            ViewManager: current ViewManager
        """
        return ViewManager()
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ViewManager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.view = None
        self.width = -1
        self.height = -1
        self.min_width = -1
        self.min_height = -1
        self.main_title = ""
        pass
    
    def set_view(self, view : View) -> None:
        self.view = view
        
    def set_width(self, width : int) -> None:
        pass
    
    def set_height(self, height : int) -> None:
        pass
    
    def set_min_width(self, min_width : int) -> None:
        pass
    
    def set_min_height(self, min_height : int) -> None:
        pass
    
    def set_main_title(self, title : str) -> None:
        pass