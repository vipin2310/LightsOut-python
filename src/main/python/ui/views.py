import PySimpleGUI as sg

if __name__ == "__main__":
    layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Demo")

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()
    
class View:
    """ Super class for creating a view with PySimpleGUI.
    """

    def __init__(self) -> None:
        """Constructor.
        """
        
        self.title = self.create_title()
        self.layout = self.create_layout()
    
    def create_layout(self) -> list:
        """Creates the layout for the GUI.

        Returns:
            list: returns the layout as a list
        """
        pass
    
    def create_title(self) -> str:
        """Creates the title for the GUI.

        Returns:
            str: returns the title as str
        """
        pass

class MainMenuView(View):
    def create_layout(self) -> list:
        return super().create_layout()
    
    def create_title(self) -> str:
        return "Main Menu"