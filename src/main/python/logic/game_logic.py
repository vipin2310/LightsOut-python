from ui.models.light_model_container import LightModelContainer
from random import randint
import numpy as np

class GameLogic:
    
    start_problem = None
        
    def set_new_start_problem(field : LightModelContainer) -> None:
        
        # Use prime number as iterations to prevent all lights out already
        GameLogic.start_problem = list(map(lambda i : (randint(0, field._num_cols - 1), randint(0, field._num_rows - 1)), range(47)))
        list(map(lambda position : GameLogic.iterate(field, position), GameLogic.start_problem))
    
    def reset_start_problem(field : LightModelContainer) -> None:
        
        if GameLogic.start_problem != None:
            light_on_lm = list(filter(lambda lm : lm.get_light_on(), field._light_models.flatten().tolist()))
            
            # Turn all lights off first
            list(map(lambda lm : lm.set_light_on(False), light_on_lm))
            
            # Reapply start problem iteration
            list(map(lambda position : GameLogic.iterate(field, position), GameLogic.start_problem))
            
    
    def iterate(field : LightModelContainer, position : tuple[int, int]) -> None:
        field.get_light_model(position).toggle_light_on()    
        neighbors = field.get_neighbors(position)
    
        # Using map function to replace for-loop
        neighbors[:] = map(lambda lm : lm.toggle_light_on() if lm != None else lm, neighbors)
    
    def is_field_solved(field : LightModelContainer) -> bool:
        light_on_lm = list(filter(lambda lm : lm.get_light_on(), field._light_models.flatten().tolist()))
        return len(light_on_lm) == 0