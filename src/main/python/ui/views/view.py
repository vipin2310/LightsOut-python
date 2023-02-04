import PySimpleGUI as sg
from ui.controllers.controller import Controller

class View:
    """ Super class for creating a view with PySimpleGUI.
    """

    def __init__(self) -> None:
        """Constructor.
        """
        
        self.main_title = ""
        self.title = self._create_title()
        self.layout = self._create_layout()
        self.controller = self._create_controller()
        self.window_created = False
        
        self.resizable = False
        self._min_width = 0
        self._min_height = 0
        self.element_padding = None
    
    def create_window(self) -> None:
        """Creates the window specified by the view.
        """
        
        self.window_created = True
        
        title = self.title if len(self.main_title) == 0 else f"{self.main_title}: {self.title}"
        self.window = sg.Window(title, self.layout, resizable=self.resizable, finalize=True, element_padding=self.element_padding)
        
        self._finalized()
    
    def close_window(self) -> None:
        """Closes the window specified by the view.
        """
        
        self.window_created = False
        if not self.window.is_closed():
            self.window.close()
        
    def set_width(self, width : int) -> None:
        """Sets the current width of the window.

        Args:
            width (int): The width of the window.
        """
        
        self.window.size = (width, self.window.size[1])
    
    def set_height(self, height : int) -> None:
        """Sets the current height of the window.

        Args:
            height (int): The height of the window.
        """
        
        self.window.size = (self.window.size[0], height)
    
    def set_min_width(self, min_width : int) -> None:
        """Sets the minimum width of the window.

        Args:
            min_width (int): The minimum width of the window.
        """
        
        self._min_width = min_width
        self.window.set_min_size((self._min_width, self._min_height))
    
    def set_min_height(self, min_height : int) -> None:
        """Sets the minimum height of the window.

        Args:
            min_height (int): The minimum height of the window.
        """
        
        self._min_height = min_height
        self.window.set_min_size((self._min_width, self._min_height))
    
    def set_main_title(self, main_title : str) -> None:
        """Sets the title for this window.

        Args:
            title (str): The title for the window.
        """
        
        self.main_title = main_title
        self.window.set_title(f"{self.main_title}: {self.title}")
    
    def read_events(self) -> None:
        """Reads events of the view and passes it to the controller.
        """
        
        event, values = self.window.read()
        self.controller.handle_event(event)
        
    def _create_controller(self) -> Controller:
        """Creates the controller for the GUI

        Returns:
            Controller: controller
        """
        
        pass
    
    def _create_layout(self) -> list:
        """Creates the layout for the GUI.

        Returns:
            list: returns the layout as a list
        """
        pass
    
    def _create_title(self) -> str:
        """Creates the title for the GUI.

        Returns:
            str: returns the title as str
        """
        pass
    
    def _finalized(self) -> None:
        
        pass