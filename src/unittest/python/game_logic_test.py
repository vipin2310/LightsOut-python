import unittest
import copy
from logic.game_logic import GameLogic
from ui.models.light_model_container import LightModelContainer

class GameLogicTest(unittest.TestCase):
    """
    Tests the GameLogic class of this project.
    """
    
    def test_set_new_start_problem(self):
        field = LightModelContainer(button_size=(1, 1), num_rows=5, num_cols=5)
        GameLogic.set_new_start_problem(field)
        
        # GameLogic should save the last set start problem
        self.assertIsNotNone(GameLogic.start_problem)
        
        all_lights_off = True
        for y in range(5):
            for x in range(5):
                position = (x, y)
                lm = field.get_light_model(position)
                
                if lm._light_on:
                    all_lights_off = False
                    break
        
        # At least one light should be on
        self.assertFalse(all_lights_off)
        
    def test_reset_start_problem(self):
        field = LightModelContainer(button_size=(1, 1), num_rows=5, num_cols=5)
        fieldDeepCopy = copy.deepcopy(field)
        
        # Set a start problem
        GameLogic.set_new_start_problem(field)
        
        # Reset the deep copy to this start problem
        GameLogic.reset_start_problem(fieldDeepCopy)
        
        allEqual = True
        for y in range(5):
            for x in range(5):
                position = (x, y)
                lm1 = field.get_light_model(position)
                lm2 = fieldDeepCopy.get_light_model(position)
                
                if lm1._light_on != lm2._light_on:
                    allEqual = False
                    break
        
        self.assertTrue(allEqual)
    
    def test_iterate(self):
        field = LightModelContainer(button_size=(1, 1), num_rows=5, num_cols=5)
        GameLogic.iterate(field, (0, 0))
        GameLogic.iterate(field, (3, 3))
        
        """
        Should be like this:
        
        O  O  .  .  .
        O  .  .  .  .
        .  .  .  O  .
        .  .  O  O  O
        .  .  .  O  .
        
        """
        
        # Check if the correct positions are on
        positions_on = [(0, 0), (1, 0), (0, 1), (3, 2), (2, 3), (3, 3), (4, 3), (3, 4)]
        for y in range(5):
            for x in range(5):
                position = (x, y)
                lm = field.get_light_model(position)
                
                if position in positions_on:
                    self.assertTrue(lm._light_on)
                else:
                    self.assertFalse(lm._light_on)
                    
    def test_is_field_solved(self):
        field = LightModelContainer(button_size=(1, 1), num_rows=5, num_cols=5)
        
        # Initialized field should already be solved
        self.assertTrue(GameLogic.is_field_solved(field))