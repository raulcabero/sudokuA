"""
Author: Maria Ledezma
Creation Date: 07/01/2013
"""
import inspect
import re
import os.path
import xml.etree.ElementTree as ET

class Configuration():
    """Super class that manipulates the configuration file for Sudoku game"""

    def __init__(self, config_file_name):
        """constructor that sets the name and path_name of the configuration file.

            Keyword arguments:
            config_file_name -- the name of the configuration file

        """
        self.file_name = config_file_name
        self.base_path = self.get_base_path()
        self.path_name = self.base_path + self.file_name

    def get_base_path(self):
        """Gets the base path of the configuration file"""
        file_path_inspect = inspect.getouterframes(inspect.currentframe())[1][1]
        file_path_inspect = os.path.abspath(file_path_inspect)
        base_path = re.findall(r'(.+SudokuA\\)', file_path_inspect)[0]
        return base_path

    def read_configuration_file(self):
        """Abstract method: Reads the configuration file defined in the constructor.
           Definition and more codumentation in the child class.

        """
        raise Exception("Define this method in a sub-class")

    def modify_complexity(self, complexity):
        """Abstract method - Modifies the complexity in the configuration file.
           Definition and more codumentation in the child class.

            Keyword arguments:
            complexity -- the complexity of the game e.g. 'hard'

        """
        raise Exception("Define this method in a sub-class")
     
    def modify_output_type(self, output_type):
        """Abstract method - Modifies the output type of the solution in the 
                            configuration file.
           Definition and more codumentation in the child class.

            Keyword arguments:
            output_type -- the type of the output of the game e.g. 'console'
            
        """
        raise Exception("Define this method in a sub-class")

    def modify_algorithm(self, algorithm):
        """Abstract method - Modifies the algorithm for Sudoku solution in the 
                            configuration file.
           Definition and more codumentation in the child class.

            Keyword arguments:
            algorithm -- the algorithm to be used in the game e.g. 'norvig'
            
        """
        raise Exception("Define this method in a sub-class")

    def get_complexity(self):
        """Abstract method - Returns the complexity set in the configuration
                            file e.g. 'hard' """
        raise Exception("Define this method in a sub-class")

    def get_output_type(self):
        """Abstract method - Returns the output type set in the configuration 
                            file e.g. 'file' """
        raise Exception("Define this method in a sub-class")

    def get_algorithm(self):
        """Abstract method - Returns the algorithm set in the configuration 
                            file e.g. 'norvig' 

        """
        raise Exception("Define this method in a sub-class")

    def get_space_char(self):
        """Abstract method - Returns the character used as space set in the
           configuration file e.g. '0' 

        """
        raise Exception("Define this method in a sub-class")