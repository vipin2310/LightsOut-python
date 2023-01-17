class Controller:
    def __init__(self, view):
        """Constructor.

        Args:
            view (View): The underlying view for this controller.
        """
        self.view = view
        
    def handle_event(self, event : str) -> None:
        """Handles events for the view

        Args:
            event (str): The event to be handled represented as a string
        """
        
        pass
    