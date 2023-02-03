class LightModel:
    """
    The LightModel for a button which updates the listeners (LightFieldButton) if internal value is changed.
    """
    
    def __init__(self, light_on : bool):
        self._light_on = light_on
        self._listeners = []
    
    def add_listener(self, listener):
        self._listeners.append(listener)
    
    def set_light_on(self, light_on : bool) -> None:
        self._light_on = light_on
        
        for listener in self._listeners:
            listener.light_model_changed()
    
    def get_light_on(self) -> bool:
        return self._light_on
    
    def toggle_light_on(self) -> None:
        self.set_light_on(not self._light_on)