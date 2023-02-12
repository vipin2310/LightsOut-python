from ui.models.light_model_container import LightModelContainer
from random import randint

class GameLogic:
    """
    Implementing the logic for the game, such as creating a start problem or iterating after one click.
    """
    start_problem = None
    
    @staticmethod
    def set_new_start_problem(field : LightModelContainer) -> None:
        """
        Sets a new start problem in the LightModelContainer to be solved by the player.

        Parameters
        ----------
        field : LightModelContainer
            The container containing the LightModels that represent the state of the displayed grid.
        """
        
        # Use prime number as iterations to prevent all lights out already
        prime_number_iter = 47
        GameLogic.start_problem = list(map(lambda i : (randint(0, field._num_cols - 1), randint(0, field._num_rows - 1)), range(prime_number_iter)))
        list(map(lambda position : GameLogic.iterate(field, position), GameLogic.start_problem))
    
    @staticmethod
    def reset_start_problem(field : LightModelContainer) -> None:
        """
        Resets the grid to the last setted start problem.

        Parameters
        ----------
        field : LightModelContainer
            The container which the start problem should be applied to.
        """
        
        if GameLogic.start_problem != None:
            light_on_lm = list(filter(lambda lm : lm.get_light_on(), field._light_models.flatten().tolist()))
            
            # Turn all lights off first
            list(map(lambda lm : lm.set_light_on(False), light_on_lm))
            
            # Reapply start problem iteration
            list(map(lambda position : GameLogic.iterate(field, position), GameLogic.start_problem))
            
    @staticmethod
    def iterate(field : LightModelContainer, position : tuple[int, int]) -> None:
        """
        Iterates on the LightModelContainer after one position is selected by the player.

        Parameters
        ----------
        field : LightModelContainer
            The container which the logic should be applied to.
        position : tuple[int, int]
            The position which will be used to iterate / toggle.
        """
        field.get_light_model(position).toggle_light_on()    
        neighbors = field.get_neighbors(position)
    
        # Using map function to replace for-loop
        neighbors[:] = map(lambda lm : lm.toggle_light_on() if lm != None else lm, neighbors)
    
    @staticmethod
    def is_field_solved(field : LightModelContainer) -> bool:
        """
        Checks if the field is already solved according to the game logic.

        Parameters
        ----------
        field : LightModelContainer
            The field which contains the LightModels that represent the current state of the grid.

        Returns
        -------
        bool
            True if solved, else False.
        """
        light_on_lm = list(filter(lambda lm : lm.get_light_on(), field._light_models.flatten().tolist()))
        return len(light_on_lm) == 0