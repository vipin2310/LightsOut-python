from ui.views.view import View
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
        """Prevents the creation of new instances if there is already one.

        Returns:
            ViewManager instance.
        """
        
        if not hasattr(cls, 'instance'):
            cls.instance = super(ViewManager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        """Constructor.
        """
        
        self.view = None
        self.width = -1
        self.height = -1
        self.min_width = -1
        self.min_height = -1
        self.main_title = ""
        self.terminated = False
    
    def set_view(self, view : View) -> None:
        """Sets a new view for the application. Closes the previous view.

        Args:
            view (View): The view to be set.
        """
        
        if self.view != None:
            self.view.close_window()
        
        self.view = view
        self.view.create_window()
        
    def set_width(self, width : int) -> None:
        """Sets the current width of the application window.

        Args:
            width (int): The width of the application window.
        """
        
        self.width = width
        self.view.set_width(self.width)
    
    def set_height(self, height : int) -> None:
        """Sets the current height of the application window.

        Args:
            height (int): The height of the application window.
        """
        
        self.height = height
        self.view.set_height(height)
    
    def set_min_width(self, min_width : int) -> None:
        """Sets the minimum width of the application window.

        Args:
            min_width (int): The minimum width of the application window.
        """
        
        self.min_width = min_width
        self.view.set_min_width(self.min_width)
    
    def set_min_height(self, min_height : int) -> None:
        """Sets the minimum height of the application window.

        Args:
            min_height (int): The minimum height of the application window.
        """
        
        self.min_height = min_height
        self.view.set_min_height(self.min_height)
    
    def set_main_title(self, main_title : str) -> None:
        """Sets the title for this application window.

        Args:
            main_title (str): The title for the application window.
        """
        
        self.main_title = main_title
        self.view.set_main_title(self.main_title)
        
    def start_event_handler(self) -> None:
        self.view.read_events()
        
    def terminate(self) -> None:
        if not self.terminated and self.view != None:
            self.terminated = True
            self.view.close_window()