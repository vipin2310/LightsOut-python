from ui.models.light_model_container import LightModelContainer
from random import randint
import numpy as np

class GameLogic:
    
    def set_start_problem(field : LightModelContainer) -> None:
        for i in range(50):
            random_x = randint(0, field._num_cols - 1)
            random_y = randint(0, field._num_rows - 1)
            
            GameLogic.iterate(field, (random_x, random_y))
            
    def iterate(field : LightModelContainer, position : tuple[int, int]) -> None:
        field.get_light_model(position).toggle_light_on()    
        neighbors = field.get_neighbors(position)
    
        # Using map function to replace for-loop
        neighbors[:] = map(lambda lm : lm.toggle_light_on() if lm != None else lm, neighbors)
    
    def is_field_solved(field : LightModelContainer) -> bool:
        light_on_lm = list(filter(lambda lm : lm.get_light_on(), field._light_models.flatten().tolist()))        
        return len(light_on_lm) == 0