# LightsOut-python
Project for advanced software engineering which implements the game "Lights Out" in Python.

## 1. Git
- [Git branches](https://github.com/vipin2310/LightsOut-python/branches)
- [Git commits](https://github.com/vipin2310/LightsOut-python/commits)

## 2. Unified Modeling Language (UML) 
As UML diagrams the following were chosen:
- [Class diagram](https://github.com/vipin2310/LightsOut-python/tree/main/docs/class%20diagram) &rarr; Go to [PNG](https://github.com/vipin2310/LightsOut-python/blob/main/docs/class%20diagram/UML_class_diagram.drawio.png) or [PDF](https://github.com/vipin2310/LightsOut-python/blob/main/docs/class%20diagram/UML_class_diagram.drawio.pdf)
- [Package diagram](https://github.com/vipin2310/LightsOut-python/tree/main/docs/package%20diagram) &rarr; Go to [PNG](https://github.com/vipin2310/LightsOut-python/blob/main/docs/package%20diagram/UML_package_diagram.png) or [PDF](https://github.com/vipin2310/LightsOut-python/blob/main/docs/package%20diagram/UML_package_diagram.pdf)
- [Use case diagram](https://github.com/vipin2310/LightsOut-python/tree/main/docs/use%20case%20diagram) &rarr; Go to [PNG](https://github.com/vipin2310/LightsOut-python/blob/main/docs/use%20case%20diagram/UML_use%20case%20diagram.png) or [PDF](https://github.com/vipin2310/LightsOut-python/blob/main/docs/use%20case%20diagram/UML_use%20case%20diagram.pdf)

The tool [draw.io (now diagrams.net)](https://www.diagrams.net) was used to create these.
The class diagram represents the relationship between the classes in the project.
For the package diagram and the use case diagram the project was pumped up artificially as if the funds of Edlich-Investment were used.

## 3. Domain Driven Design (DDD)
A [Miro](https://miro.com)-Board was used for Event storming, creating a Core Domain Chart and indicating the relationship between the domains to apply the Domain Driven Design in this project.
- [See the PDF-file for the Event storming and Domain modeling](https://github.com/vipin2310/LightsOut-python/blob/main/docs/domain%20driven%20design.pdf)

## 4. Metrices
The metrices will be calculated by [SonarCloud](https://sonarcloud.io) after every push to the main branch in GitHub. Therefore the metrices are always up-to date with the code from the main branch.

Sonarcloud scans all the code located in [/src/main/python/](https://github.com/vipin2310/LightsOut-python/tree/main/src/main/python)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)


[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=vipin2310_LightsOut-python)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)

## 5. Clean Code Development

### Part A: CCD used in this project
- Don't repeat yourself (DRY) 

    &rarr; [Example 1: Use of constant to store repeating value](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/view_manager.py#L17)

    &rarr; [Example 2: Use of function to prevent repeating expression](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/controllers/light_field_game_view_controller.py#L77)

- Single level of abstraction 

    &rarr; [Example 1: GameLogic.iterate()](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/logic/game_logic.py#L46)

    &rarr; [Example 2: LightFieldButton._get_sized_button_image()](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/components/light_field_button.py#L59)

- Usage of common design patterns &rarr;

    &rarr; Example 1: Model-View-Controller (MVC): [Model](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/models/light_model.py), [View](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/views/light_field_game_view.py), [Controller](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/controllers/light_field_game_view_controller.py)

    &rarr; Example 2: Observer-Pattern: [Observer](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/components/light_field_button.py), [Observable](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/models/light_model.py)

- Separation of concerns 

    &rarr; Example: Package structure: [logic](https://github.com/vipin2310/LightsOut-python/tree/main/src/main/python/logic), [ui](https://github.com/vipin2310/LightsOut-python/tree/main/src/main/python/ui)

- Small functions with descriptive names 

    &rarr; [Example 1: Method with boolean return type, prefix is](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/logic/game_logic.py#L64)

    &rarr; [Example 2: Expose return value in name](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/models/light_model_container.py#L34)

- Use of docstrings

    &rarr; [Example: ViewManager class](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/view_manager.py)

    &rarr; And many more, look through the project

### Part B: CCD cheat sheet
- [Go to my personal Clean Code Development Cheat Sheet with 10 principles.](https://github.com/vipin2310/LightsOut-python/blob/main/docs/clean%20code/CCD_CheatSheet.pdf)

## 6. Build Management
[PyBuilder](https://pybuilder.io) is used as the build automation/management tool for this project.
The project file structure was created according to PyBuilder's ecosystem.
With this tool the command `pyb` can be executed on this project, which automatically installs all dependencies and runs the unit-tests.

To analyze the behaviour of PyBuilder you can have a look in [build.py](https://github.com/vipin2310/LightsOut-python/blob/main/build.py).

## 7. Unit-Tests
The unit-tests are implemented using the unit testing framework of the Python Standard Library "[unittest](https://docs.python.org/3/library/unittest.html)". The unit tests ensure that the logic of the program stays the same throughout further development.

- [Click here to get to the directory where the unittests are located.](https://github.com/vipin2310/LightsOut-python/tree/develop/src/unittest/python)
- 4 Unittests for the game logic: &rarr; [click here](https://github.com/vipin2310/LightsOut-python/blob/develop/src/unittest/python/game_logic_test.py)
- 2 Unittests for the object containing the state of the play field &rarr; [click here](https://github.com/vipin2310/LightsOut-python/blob/develop/src/unittest/python/light_model_container_test.py)

For the UI itself there are no unit-tests implemented since most of the functions don't return a type that can be easily compared to a correct state. Nevertheless the UI is tested manually by hand to ensure that the components and the game interactions work as intended.

## 8. Continuous Delivery
In this project GitHub Actions is used to establish a CI/CD pipeline.
In the pipeline 2 jobs are being executed.
The first job is the SonarCloud analysis (see [4. Metrices](https://github.com/vipin2310/LightsOut-python#4-metrices)) which updates the metrics for the source code in the main branch.
The second job calls PyBuilder which installs the dependencies and runs the unit-tests.
After completion of the pipeline SonarCloud and PyBuilder report a successful or failed result which will be shown next to the commit in the history.
- Go to the pipeline: [build.yml](https://github.com/vipin2310/LightsOut-python/blob/main/.github/workflows/build.yml)

## 9. IDE
For this project [Visual Studio Code](https://code.visualstudio.com) was used as primary IDE.

Favourite key shortcuts:
- Show/Hide Primary Side Bar (e. g. Project explorer): `Ctrl` + `B`
- Show/Hide Lower Panel (e. g. Terminal): `Ctrl` + `J`
- Refactor code: `Ctrl` + `Shift` + `R`
- Debug project: `F5`
- Open command pallete: `Ctrl` + `Shift` + `P`
- Rename variable/function/etc.: `F2`

## 10. Domain-specific language (DSL)
For domain-specific language there is a script implemented for [Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview) which setups this project and starts the game.
To setup it will be checked whether the Python version is at least 3.9 and PIP is available. Therefore to run the script Python 3.9 must be installed and the [path variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables) for Python and PIP must be configured correctly under Microsoft Windows so the script can call Python and PIP from the terminal.
After checking for the entry point of this project, PyBuilder will be installed through PIP and the build process will be started which then installs all necessary dependencies for the game and executes the unit tests as configured in [setup.py](https://github.com/vipin2310/LightsOut-python/blob/main/setup.py) and [build.py](https://github.com/vipin2310/LightsOut-python/blob/main/build.py).
At the end the [main.py](https://github.com/vipin2310/LightsOut-python/blob/main/src/main/python/main.py) file will be called which starts the game.

To start the script you can right-click on the file `setup_and_start_game.ps1` in the project path and choose the option `Run with PowerShell` in the context menu.

Unfortunately due to some edge cases with the Python installation the script must run with admin privileges to bypass the issue. This might lead to an `UnauthorizedAccess` error. To resolve this follow  point 1 under known issues below.

- [Click here to get to the Powershell script.](https://github.com/vipin2310/LightsOut-python/blob/main/setup_and_start_game.ps1)

### Known Issues
There are certain issues that can be encountered when executing the script.

1. Since the script requires admin privileges the default Windows Execution Policy will block the PS-script. To solve this issue you must set the Execution Policy to Unrestricted using this command in Powershell:

    ```
    Set-ExecutionPolicy -ExecutionPolicy Unrestricted
    ```

    To reset the ExecutionPolicy to default after you are finished you can use:

    ```
    Set-ExecutionPolicy -ExecutionPolicy Default
    ```

2. If you get the error message that the term `pyb` is not recognized it is most likely because of a previous corrupt installation of PyBuilder. To resolve this issue a reinstallation of PyBuilder might do the trick. To be on the safe side you can run this command in a terminal with admin privileges:

    ```
    pip install --force-reinstall pybuilder
    ```

## 11. Functional Programming
The aspects of Functional Programming are covered in this project. Click the aspects to see to the examples.

- [Only final data structures](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/view_manager.py#L8)

    The data for this project is stored in primitive data types such as boolean, integer, etc. and are therefore final.

- [(Mostly) Side effect free functions](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/ui/view_manager.py#L76)

    Most of the functions have no side effect and only fulfill one specific task which is visible in their name.

- [Use of higher-order functions / Functions as parameters and return values](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/logic/game_logic.py#L62)

    Instead of for-loops there are many examples where the map-function is used in combination with an anonymous function as a parameter.

- [Use closures / anonymous functions](github.com/vipin2310/LightsOut-python/blob/main/src/main/python/logic/game_logic.py#L79)

    Anonymous functions / Lambdas are used mostly in map-functions to replace for-loops.