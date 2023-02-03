import PySimpleGUI as sg
import numpy as np
from ui.components.light_field_button import LightFieldButton
from ui.models.light_model import LightModel

class LightModelContainer:
    
    def __init__(self, button_size : tuple[int, int], num_rows : int, num_cols : int) -> None:
        
        self._button_size = button_size
        self._num_rows = num_rows
        self._num_cols = num_cols
        
        self._light_models = np.array([[LightModel(False) for y in range(self._num_rows)] for x in range(self._num_cols)])
        
    def get_layout_for_view(self) -> list[sg.Column]:
        
        columns = [[[LightFieldButton(size=self._button_size, position=(x, y), light_model=self._light_models[(x, y)])] 
                    for y in range(self._num_rows)] 
                    for x in range(self._num_cols)]
        return [sg.Column(column, element_justification="c", pad=(0,0)) for column in columns]
    
    def get_light_model(self, position : tuple[int, int]) -> LightModel:
        
        if 0 <= position[0] < self._num_cols  and 0 <= position[1] < self._num_rows:
            return self._light_models[position]
        else:
            raise ValueError("The specified position is not valid for the size of the grid.")
        
    def get_neighbors(self, position : tuple[int, int]) -> list[LightModel]:
        
        x = position[0]
        y = position[1]
        
        if 0 <= x < self._num_cols and 0 <= y < self._num_rows:
            top_neighbor = self._light_models[(x, y - 1)] if y - 1 >= 0 else None
            right_neighbor = self._light_models[(x + 1, y)] if x + 1 < self._num_cols else None
            bottom_neighbor = self._light_models[(x, y + 1)] if y + 1 < self._num_rows else None
            left_neighbor = self._light_models[(x - 1, y)] if x - 1 >= 0 else None
            
            return [top_neighbor, right_neighbor, bottom_neighbor, left_neighbor]
        else:
            raise ValueError("The specified position is not valid for the size of the grid.")