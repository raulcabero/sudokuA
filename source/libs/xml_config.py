"""
Author: Maria Ledezma
Creation Date: 07/02/2013
"""
import os
import xml.etree.ElementTree as ET
from configuration import Configuration

class XMLConfig(Configuration):
    """Child class that inheritates of Configuration and handles a XML 
    configuration file for Sudoku game

    """
    def __init__(self, config_file_name = "config.xml"):
        """Constructor that calls constructor of super class Configuration and 
            forms path to game_settings

            Keyword arguments:
            config_file_name -- the name of the XML configuration file (default 
                                                                    config.xml)

        """
        Configuration.__init__(self, config_file_name)
        #definition of the path for the game_settings configuration file
        self.path_game_settings = Configuration.get_base_path(self) + "game_settings.xml"

    def write_value_to_xml(self, file_path, xml_tag_path, new_value):
        """Writes a new value in a xml file given a xml tag path
            Keyword arguments:
            file_path -- the file and path of the xml to be configured
            xml_tag_path -- the tag path in the xml file e.g. 'level/value'
            new_value -- the new value that will be set

        """
        tree = ET.parse(file_path)
        root = tree.getroot()
        root.find(xml_tag_path).text = new_value
        tree.write(file_path)

    def get_value_from_xml(self, file_path, xml_tag_path):
        """Gets the value in a xml file given a xml tag path
            Keyword arguments:
            file_path -- the file and path of the xml to be configured
            xml_tag_path -- the tag path in the xml file e.g. 'level/value'

        """
        tree = ET.parse(file_path)
        root = tree.getroot()
        text_found = root.find(xml_tag_path).text
        return text_found

    def read_configuration_file(self):
        """Reads the configuration file defined in the constructor and returns
         the data into a dictionary

        """
        try:
            config_dict = {}

            tree = ET.parse(self.path_name)
            root = tree.getroot()
            config_dict['output-type'] = root.find('outputtype/value').text
            config_dict['output-path'] = root.find('outputtype/path').text
            config_dict['algorithm'] = root.find('algorithm/value').text   
            config_dict['level'] = root.find('level/value').text
            config_dict['space_char'] = root.find('space_char/value').text

            return config_dict
        except:
            error_msg = "Invalid data or file" 
            return error_msg
    
    def get_valid_data_game(self, file_path, xml_tag_path, attrib_name):
        """Returns a list of valid data that can be iterated and have an attribute
            defined in the game_settings.xml

           Keyword arguments:
            file_path -- the file and path of the xml to get the data
            xml_tag_path -- the tag path in the xml file to be iterated e.g. 'level'
            attrib_name -- name of the attribute to collect the data e.g. 'name'

        """
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            list_items = []
            
            for item in root.iter(xml_tag_path):
                list_items.append(item.attrib[attrib_name])

            return list_items

        except:
            raise Exception('Could not retrieve data from game_settings')

    def get_complexity(self):
        """Returns the complexity defined in the XML configuration file e.g. 'easy' """
        try:
            complexity = self.get_value_from_xml(self.path_name, 'level/value')
            return complexity
        except:
            error_msg = "Tag is missing!" 
            return error_msg

    def modify_complexity(self, complexity):
        """Modifies the complexity in the XML configuration file 

           Keyword arguments:
            complexity -- the complexity of the game e.g. 'hard'

        """
        try:
            complexity = complexity.lower()

            if complexity not in self.get_valid_data_game(self.path_game_settings, 'level', 'name'):
                return "Invalid complexity parameter"

            self.write_value_to_xml(self.path_name, 'level/value', complexity)
            return "Complexity: " + complexity.upper() + " was set successfully!"
        except:
            error_msg = "Tag is missing!" 
            return error_msg

    def get_output_type(self):
        """Returns the type for the output of the game e.g. 'file' """
        try:
            output_type = self.get_value_from_xml(self.path_name, 'outputtype/value')
            return output_type
        except:
            error_msg = "Tag is missing!"
            return error_msg

    def modify_output_type(self, output_type):
        """Modifies the type of the output in the XML configuration file 

           Keyword arguments:
            output_type -- the type of the output of the game e.g. 'console'

        """
        try:
            output_type = output_type.lower()

            if output_type not in ['console', 'file']:
                return "Invalid output type parameter"
            output_path = ''
            
            if output_type == 'file':
                output_path = 'results'

            self.write_value_to_xml(self.path_name,'outputtype/value', output_type)
            self.write_value_to_xml(self.path_name,'outputtype/path', output_path)

            return "Output type: " + output_type.upper() + " was set successfully!"
        except:
            error_msg = "Tag is missing!" 
            return error_msg
    
    def modify_algorithm(self, algorithm):
        """Modifies the algorithm in the XML configuration file 

           Keyword arguments:
            algorithm -- the algorithm to be used in the game e.g. 'norvig'

        """
        try:
            algorithm = algorithm.lower()

            if algorithm not in self.get_valid_data_game(self.path_game_settings, 'algorithm', 'name'):
                return "Invalid algorithm parameter"

            self.write_value_to_xml(self.path_name, 'algorithm/value', algorithm)
            return "Algorithm: " + algorithm.upper() + " was set successfully!"
        except:
            error_msg = "Tag is missing!" 
            return error_msg

    def get_algorithm(self):
        """Returns the algorithm set in the configuration file e.g. 'norvig' """
        try:
            algorithm = self.get_value_from_xml(self.path_name, 'algorithm/value')
            return algorithm
        except:
            error_msg = "Tag is missing!"
            return error_msg
