# LightsOut-python
Project for advanced software engineering which implements the game "Lights Out" in Python.

## 1. Git
- [Git branches](https://github.com/vipin2310/LightsOut-python/branches)
- [Git commits](https://github.com/vipin2310/LightsOut-python/commits)

## 2. Unified Modeling Language (UML) 
- TODO

## 3. Domain Driven Design (DDD)
- TODO

## 4. Metrices
The metrices will be calculated after push to the main branch by SonarCloud. Therefore the metrices are always up-to date with the code from the main branch.

Sonarcloud scans all the code located in [/src/main/python/](https://github.com/vipin2310/LightsOut-python/tree/main/src/main/python)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=vipin2310_LightsOut-python&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)


[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=vipin2310_LightsOut-python)](https://sonarcloud.io/summary/new_code?id=vipin2310_LightsOut-python)

## 5. Clean Code Development
- TODO

## 6. Build Management
- PyBuilder

## 7. Unit-Tests
The unit-tests are implemented using the unit testing framework of the Python Standard Library "[unittest](https://docs.python.org/3/library/unittest.html)". The unit tests ensure that the logic of the program stays the same throughout further development.

- [Click here to get to the directory where the unittests are located.](https://github.com/vipin2310/LightsOut-python/tree/develop/src/unittest/python)
- 4 Unittests for the game logic: &rarr; [click here](https://github.com/vipin2310/LightsOut-python/blob/develop/src/unittest/python/game_logic_test.py)
- 2 Unittests for the object containing the state of the play field &rarr; [click here](https://github.com/vipin2310/LightsOut-python/blob/develop/src/unittest/python/light_model_container_test.py)

For the UI itself there are no unit-tests implemented since most of the functions don't return a type that can be easily compared to a correct state. Nevertheless the UI is tested manually by hand to ensure that the components and the game interactions work as intended.

## 8. Continuous Delivery
GitHub Actions:
- [build.yml](https://github.com/vipin2310/LightsOut-python/blob/main/.github/workflows/build.yml)

## 9. IDE
Visual Studio Code

## 10. Domain-specific language (DSL)
- TODO

## 11. Functional Programming
- TODO