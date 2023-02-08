import PySimpleGUI as sg
import numpy as np
from ui.components.light_field_button import LightFieldButton
from ui.models.light_model import LightModel

class LightModelContainer:
    """
    This class is holding the LightModels which represents the underlying 
    state of the LightField which is presented to the player.
    """
    def __init__(self, button_size : tuple[int, int], num_rows : int, num_cols : int) -> None:
        """
        The contructor of the LightFieldContainer, it creates the LightModels which can
        later be linked to the buttons.

        Parameters
        ----------
        button_size : tuple[int, int]
            The size of the buttons which will be used if the layout for the GUI will be delivered.
        num_rows : int
            Number of rows in the LightField.
        num_cols : int
            Number of columns in the LightField.
        """
        
        self._button_size = button_size
        self._num_rows = num_rows
        self._num_cols = num_cols
        
        self._light_models = np.array([[LightModel(False) 
                                        for y in range(self._num_rows)] 
                                        for x in range(self._num_cols)])
        
    def get_layout_for_view(self) -> list[sg.Column]:
        """
        Returns the Layout (the buttons) which can be clicked by the player. 
        It links the buttons to the contained LightModels by this instance.

        Returns
        -------
        list[sg.Column]
            The layout as columns.
        """
        
        columns = [[[LightFieldButton(size=self._button_size, position=(x, y), light_model=self._light_models[(x, y)])] 
                    for y in range(self._num_rows)] 
                    for x in range(self._num_cols)]
        return [sg.Column(column, element_justification="c", pad=(0,0)) for column in columns]
    
    def get_light_model(self, position : tuple[int, int]) -> LightModel:
        """
        Gets the LightModel at the specified position in this LightModelContainer.

        Parameters
        ----------
        position : tuple[int, int]
            The position in the grid.

        Returns
        -------
        LightModel
            The LightModel which sits on the position.

        Raises
        ------
        ValueError
            If the position is not contained by this LightModelContainer.
        """
        
        if 0 <= position[0] < self._num_cols  and 0 <= position[1] < self._num_rows:
            return self._light_models[position]
        else:
            raise ValueError("The specified position is not valid for the size of the grid.")
        
    def get_neighbors(self, position : tuple[int, int]) -> list[LightModel]:
        """
        Gets the neightboring LightModels from a position in the grid. (Upper, right, lower, left)

        Parameters
        ----------
        position : tuple[int, int]
            The position from which the neighbors will be returned.

        Returns
        -------
        list[LightModel]
            LightModels which are in the 4-neighbors of the position. 
            If the neighbor is not available (e. g. due to position at edge) it returns None for it.

        Raises
        ------
        ValueError
            If the specified position is not in the grid.
        """
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