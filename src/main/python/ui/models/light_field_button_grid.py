import PySimpleGUI as sg
import numpy as np
from ui.components.light_field_button import LightFieldButton

class LightFieldButtonGrid:
    
    def __init__(self, button_size : tuple[int, int], num_rows : int, num_cols : int) -> None:
        self.button_size = button_size
        self.num_rows = num_rows
        self.num_cols = num_cols
        
        self.light_field = np.array([[False for y in range(self.num_rows)] for x in range(self.num_cols)])
        self._button_grid = np.array([[LightFieldButton(light_on=False, size=self.button_size, position=(x, y)) for y in range(self.num_rows)] for x in range(self.num_cols)])
        
    def get_layout_for_view(self) -> list[sg.Column]:
        
        columns = [[[self._button_grid[x, y]] for y in range(self.num_rows)] for x in range(self.num_cols)]
        return [sg.Column(column, element_justification="c", pad=(0,0)) for column in columns]
    
    def get_button(self, position : tuple[int, int]) -> LightFieldButton:
        
        if 0 <= position[0] < self.num_cols  and 0 <= position[1] < self.num_rows:
            return self._button_grid[position]
        else:
            raise ValueError("The specified position is not valid for the size of the grid.")