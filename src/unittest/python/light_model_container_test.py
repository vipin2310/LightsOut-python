import unittest
from ui.models.light_model_container import LightModelContainer

class LightModelContainerTest(unittest.TestCase):
    """
    Tests the LightModelContainer class of this project.
    """
    
    def test_get_light_model(self):
        field = LightModelContainer((1, 1), num_rows=5, num_cols=5)
        
        # Check for valid cases
        self.assertIsNotNone(field.get_light_model((0, 0)))
        self.assertIsNotNone(field.get_light_model((0, 1)))
        self.assertIsNotNone(field.get_light_model((2, 2)))
        self.assertIsNotNone(field.get_light_model((4, 4)))
        
        # Check for Error cases
        with self.assertRaises(ValueError):
            field.get_light_model((5, 0))
        with self.assertRaises(ValueError):
            field.get_light_model((-1, 0))
            
    def test_get_neighbors(self):
        field = LightModelContainer((1, 1), num_rows=5, num_cols=5)
        
        # All neihbors must be not none
        neighbors = field.get_neighbors((2, 2))
        for neighbor in neighbors:
            self.assertIsNotNone(neighbor)
            
        # Test with a 2 none cases (order must be upper, right, bottom, left)
        neighbors = field.get_neighbors((0, 0))
        self.assertIsNone(neighbors[0])
        self.assertIsNotNone(neighbors[1])
        self.assertIsNotNone(neighbors[2])
        self.assertIsNone(neighbors[3])