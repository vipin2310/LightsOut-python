class LightModel:
    """
    The LightModel for a button which updates the listeners (LightFieldButton) if internal value is changed.
    Holds the underlying state for the game logic.
    """
    
    def __init__(self, light_on : bool):
        """
        Creates a LightModel which holds the light on state.

        Parameters
        ----------
        light_on : bool
            The starting value of this LightModel
        """
        
        self._light_on = light_on
        self._listeners = []
    
    def add_listener(self, listener):
        """
        Adds an object as listener to this LightModel (Observer pattern).

        Parameters
        ----------
        listener : Any
            Instance of an object. It should contain the light_model_changed 
            function which will be called if this LightModels state gets changed.
        """
        self._listeners.append(listener)
    
    def set_light_on(self, light_on : bool) -> None:
        """
        Sets the current state of this LightModel and triggers the changed event of the listeners.

        Parameters
        ----------
        light_on : bool
            The next light_on state for this button.
        """
        self._light_on = light_on
        
        for listener in self._listeners:
            listener.light_model_changed()
    
    def get_light_on(self) -> bool:
        """
        Gets the light_on state of this button as a boolean value.

        Returns
        -------
        bool
            True if light is on, else False.
        """
        
        return self._light_on
    
    def toggle_light_on(self) -> None:
        """
        Toggles the state of the button, so it changes the light_on state to on if it is off and vice versa.
        Triggers the changed event of the listeners.
        """
        self.set_light_on(not self._light_on)