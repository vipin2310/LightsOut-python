class Controller:
    def __init__(self, view):
        """
        Constructor

        Parameters
        ----------
        view : View
            The underlying view for this controller.
        """
        
        self.view = view
        
    def handle_event(self, event : str, values : dict) -> None:
        """
        Handles events for the view

        Parameters
        ----------
        event : str
            The event to be handled represented as a string
        values : dict
            Values that can be passed to the event handler
        """        
        
        pass
    