import PySimpleGUI

class ViewManager:
    """Manages the views for the game. This class follows the Singleton pattern.
    """
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ViewManager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, view):
        self.view