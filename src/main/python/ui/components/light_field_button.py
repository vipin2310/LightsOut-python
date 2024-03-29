import PySimpleGUI as sg
from PIL import Image
import io
import base64
from ui.models.light_model import LightModel

class LightFieldButton(sg.Button):
    """
    Implements the component for the buttons in the grid to be clicked by the player.
    """
    
    # Base64 representation of images for this button
    light_on_base64 = b'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'
    light_off_base64 = b'iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAYAAAA9zQYyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAASdEVYdFNvZnR3YXJlAEdyZWVuc2hvdF5VCAUAAAHdSURBVHhe7dJBEQAwEAOhSo/zq48dHjjgbTuoEJoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGaFKFJEZoUoUkRmhShSRGakN0HwYP75gP6x54AAAAASUVORK5CYII='
    
    def __init__(self, size : tuple[int, int], position : tuple[int, int], light_model : LightModel = None):
        """
        Creates an instance of a LightFieldButton which will present an image to the user.

        Parameters
        ----------
        size : tuple[int, int]
            The size for the button.
        position : tuple[int, int]
            The position of this button in the grid.
        light_model : LightModel, optional
            LightModel which will manage the light_on state of this button.
        """
        
        self.light_model = light_model if light_model != None else LightModel(False)
        self.light_model.add_listener(self)
        
        self._size = size
        button_image = self._get_sized_button_image()
        
        super().__init__(use_ttk_buttons=False,image_data=button_image, pad=(0, 0), key=position)
    
    def get_light_on(self) -> bool:
        """
        Retrieves the light_on/off status of this button.

        Returns
        -------
        bool
            True means light on and false means light off.
        """
        
        return self.light_model.get_light_on()
        
    def light_model_changed(self) -> None:
        """
        Event which will be triggered by the LightModel if its state got changed. 
        Updates the image data according to the LightModel.
        """
        
        button_image = self._get_sized_button_image()
        self.update(image_data = button_image)
    
    def _get_sized_button_image(self) -> None:
        """
        Gets the updated image for this button according to this instances properties.

        Returns
        -------
        bytes
            The image according to the attributes.
        """
        image = LightFieldButton.light_on_base64 if self.get_light_on() else LightFieldButton.light_off_base64
        return LightFieldButton.resize_base64_image(image, self._size)
    
    @staticmethod
    def resize_base64_image(image64 : bytes, size : tuple[int, int]) -> bytes:
        """
        Helper method to resize a base64 encoded image to a specific size.

        Parameters
        ----------
        image64 : bytes
            The image encoded in the base64 format
        size : tuple[int, int]
            The size which the image should take

        Returns
        -------
        bytes
            The resized base64 endoded image.
        """
        
        image_file = io.BytesIO(base64.b64decode(image64))
        img = Image.open(image_file)
        img.thumbnail(size, Image.ANTIALIAS)
        bio = io.BytesIO()
        img.save(bio, format='PNG')
        imgbytes = bio.getvalue()
        return imgbytes