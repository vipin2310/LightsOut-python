from ui.views.view import View

class ViewManager:
    """Manages the views for the game.
    """
    
    # Variables for the ViewManager
    _view : View = None
    _width : int = -1
    _height : int = -1
    _min_width : int = -1
    _min_height : int = -1
    _main_title : str = ""
    _terminated : bool = False
    
    def set_view(view : View, keep_attributes = True) -> None:
        """Sets a new view for the application. Closes the previous view. If wanted, the last set attributes will be applied to the next view.

        Args:
            view (View): The view to be set.
        """
        
        if ViewManager._view != None:
            ViewManager._view.close_window()
        
        ViewManager._view = view
        ViewManager._view.create_window()
        
        if keep_attributes:
            if -1 in (ViewManager._width, ViewManager._height, ViewManager._min_width, ViewManager._min_height):
                raise ValueError("One or more attributes have not been specified. Maybe you want to set keep_attributes to False.")
            
            ViewManager._view.set_width(ViewManager._width)
            ViewManager._view.set_height(ViewManager._height)
            ViewManager._view.set_min_width(ViewManager._min_width)
            ViewManager._view.set_min_height(ViewManager._min_height)
        
    def set_width(width : int) -> None:
        """Sets the current width of the application window.

        Args:
            width (int): The width of the application window.
        """
        if not ViewManager._view:
            raise ValueError("The view must be initialized first.")
        
        ViewManager._width = width
        ViewManager._view.set_width(width)
    
    def set_height(height : int) -> None:
        """Sets the current height of the application window.

        Args:
            height (int): The height of the application window.
        """
        if not ViewManager._view:
            raise ValueError("The view must be initialized first.")
        
        ViewManager._height = height
        ViewManager._view.set_height(height)
    
    def set_min_width(min_width : int) -> None:
        """Sets the minimum width of the application window.

        Args:
            min_width (int): The minimum width of the application window.
        """
        if not ViewManager._view:
            raise ValueError("The view must be initialized first.")
        
        ViewManager._min_width = min_width
        ViewManager._view.set_min_width(min_width)
    
    def set_min_height(min_height : int) -> None:
        """Sets the minimum height of the application window.

        Args:
            min_height (int): The minimum height of the application window.
        """
        if not ViewManager._view:
            raise ValueError("The view must be initialized first.")
        
        ViewManager._min_height = min_height
        ViewManager._view.set_min_height(min_height)
    
    def set_main_title(main_title : str) -> None:
        """Sets the title for this application window.

        Args:
            main_title (str): The title for the application window.
        """
        if not ViewManager._view:
            raise ValueError("The view must be initialized first.")
        
        ViewManager._main_title = main_title
        ViewManager._view.set_main_title(main_title)
        
    def start_event_handler() -> None:
        """Starts the event handling for the current view.
        """
        if not ViewManager._view:
            raise ValueError("The view must be initialized first.")
        
        ViewManager._view.read_events()
        
    def terminate() -> None:
        if not ViewManager._terminated and ViewManager._view != None:
            ViewManager._terminated = True
            ViewManager._view.close_window()