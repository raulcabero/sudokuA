"""
Author: Maria Ledezma
Creation Date: 07/01/2013
"""
import unittest
import os
import sys
import shutil
sys.path.append( '../libs' )
from xml_config import XMLConfig

class TestXmlConfig(unittest.TestCase):

    def setUp(self):
        self.xml_config = XMLConfig()
        self.path_game_settings = os.path.abspath("..\\..\\game_settings.xml")
        shutil.copy2(self.xml_config.path_name, 'copy_config.xml')
        shutil.copy2(self.path_game_settings, 'copy_game_settings.xml')

    #################################
    # Tests for: read_configuration_file(self)
    #################################

    def test_read_configuration_file_returns_error_msg_if_file_config_does_not_exist(self):
        expected_message = "Invalid data or file"
        os.remove(self.xml_config.path_name)
        self.assertEquals(expected_message, self.xml_config.read_configuration_file())
        

    def test_read_configuration_file_returns_error_msg_if_file_config_is_empty(self):
        expected_message = "Invalid data or file"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.\
                                                    read_configuration_file())

    def test_read_configuration_file_returns_error_msg_if_file_config_cannot_parse_xml(self):
        expected_message = "Invalid data or file"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><level>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.read_configuration_file())      

    def test_read_configuration_file_returns_error_msg_if_file_config_without_output_type(self):
        expected_message = "Invalid data or file"
        file_name = "test_xmls\\config_test_no_ouput_type.xml"
        shutil.copy2(file_name, "..\\..\\config_test_no_ouput_type.xml")
        config_test = XMLConfig(file_name)
        self.assertEquals(expected_message, config_test.read_configuration_file())

    def test_read_configuration_file_returns_error_msg_if_file_config_without_algorithm(self):
        expected_message = "Invalid data or file"
        file_name = "test_xmls\\config_test_no_algorithm.xml"
        shutil.copy2(file_name, "..\\..\\config_test_no_algorithm.xml")
        config_test = XMLConfig(file_name)
        self.assertEquals(expected_message, config_test.read_configuration_file())

    def test_read_configuration_file_returns_a_dictionary_of_configuration_if_valid_data(self):
        dict_configuration = {'space_char':'0', 'output-type': 'file', 
                              'algorithm': 'backtracking', 'output-path': 'results',
                               'level': 'medium'}
        self.assertEquals(dict_configuration, self.xml_config.read_configuration_file())

    ########### END read_configuration_file ##############

    #################################
    # Tests for: get_valid_data_game(self, file_path, xml_tag_path, attrib_name)
    #################################

    def test_get_valid_data_game_returns_list_of_levels_if_level_specified(self):
        expected_levels = ['easy', 'medium', 'hard']
        self.assertEquals(expected_levels, self.xml_config.get_valid_data_game(self.path_game_settings, 'level', 'name'))

    def test_get_valid_data_game_returns_list_of_algorithms_if_algorithm_specified(self):
        expected_algorithms = ['backtracking', 'norvig', 'x']
        self.assertEquals(expected_algorithms, self.xml_config.get_valid_data_game(self.path_game_settings, 'algorithm', 'name'))

    ########### END get_valid_data_game ##############

    #################################
    # Tests for: get_complexity(self)
    #################################

    def test_get_complexity_returns_error_message_if_level_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><tessst>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.get_complexity())

    def test_get_complexity_returns_complexity_value_if_value_exists(self):
        expected_default_level = 'medium'
        self.assertEquals(expected_default_level, self.xml_config.get_complexity())        

    ########### END get_complexity ##############

    #################################
    # Tests for: modify_complexity(self, complexity)
    #################################
    
    def test_modify_complexity_returns_error_message_if_level_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><level>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.modify_complexity('hard'))
    
    def test_modify_complexity_returns_error_message_if_value_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><level>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.modify_complexity('hard'))

    def test_modify_complexity_returns_error_message_if_complexity_is_not_valid(self):
        expected_message = "Invalid complexity parameter"
        self.assertEquals(expected_message, self.xml_config.modify_complexity('not-valid'))

    def test_modify_complexity_saves_new_complexity_in_config_file_if_complexity_is_valid(self):
        expected_complexity = 'hard'
        self.xml_config.modify_complexity('hard')
        current_complexity = self.xml_config.get_complexity()
        self.assertEquals(expected_complexity, current_complexity)        

    ########### END modify_complexity ##############

    #################################
    # Tests for: get_output_type(self)
    #################################

    def test_get_output_type_returns_error_message_if_level_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><tessst>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.get_output_type())

    def test_get_output_type_returns_output_type_value_if_value_exists(self):
        expected_default_output = 'file'
        self.assertEquals(expected_default_output, self.xml_config.get_output_type())        

    ########### END get_output_type ##############

    #################################
    # Tests for: modify_output_type(self, output_type)
    #################################
    
    def test_modify_output_type_returns_error_message_if_output_type_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><level>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.modify_output_type('console'))
    
    def test_modify_output_type_returns_error_message_if_path_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><level>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.modify_output_type('console'))

    def test_modify_output_type_returns_error_message_if_out_put_is_not_valid(self):
        expected_message = "Invalid output type parameter"
        self.assertEquals(expected_message, self.xml_config.modify_output_type('not-valid'))

    def test_modify_output_type_saves_console_output_type_in_config_file_if_output_type_is_console(self):
        expected_output_type = 'console'
        self.xml_config.modify_output_type('console')
        current_output_type = self.xml_config.get_output_type()
        self.assertEquals(expected_output_type, current_output_type)        

    ########### END modify_output_type ############## 

    #################################
    # Tests for: write_value_to_xml(file_path, xml_path, new_value)
    #################################
    
    def test_write_value_to_xml_modifies_complexity_to_hard_in_config_file(self):
        expected_complexity = 'hard'
        self.xml_config.write_value_to_xml(self.xml_config.path_name, 'level/value','hard')
        current_complexity = self.xml_config.get_complexity()
        self.assertEquals(expected_complexity, current_complexity)

    ########### END write_value_in_config_file ##############       

    #################################
    # Tests for: get_value_from_xml(file_path, xml_path)
    #################################
    
    def test_get_value_from_xml_recovers_complexity_from_config_file(self):
        expected_complexity = 'medium'
        complexity = self.xml_config.get_value_from_xml(self.xml_config.path_name, 'level/value')
        self.assertEquals(expected_complexity, complexity)

    ########### END get_value_from_xml ############## 

    #################################
    # Tests for: get_algorithm(self)
    #################################

    def test_get_algorithm_returns_error_message_if_algorithm_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<none>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.get_algorithm())

    def test_get_algorithm_returns_default_algorithm_value_if_value_exists(self):
        expected_default_algorithm = 'backtracking'
        self.assertEquals(expected_default_algorithm, self.xml_config.get_algorithm())        

    ########### END get_algorithm ##############

    #################################
    # Tests for: modify_algorithm(self, algorithm):
    #################################

    def test_modify_algorithm_returns_error_message_if_algorithm_tag_does_not_exist(self):
        expected_message = "Tag is missing!"
        file_config = open(self.xml_config.path_name, 'w')
        file_config.write('<config><ss>')
        file_config.close()
        self.assertEquals(expected_message, self.xml_config.modify_algorithm('backtracking'))

    def test_modify_algorithm_returns_error_message_if_algorithm_is_not_valid(self):
        expected_message = "Invalid algorithm parameter"
        self.assertEquals(expected_message, self.xml_config.modify_algorithm('not-valid'))

    def test_modify_algorithm_saves_norvig_in_config_file_if_algorithm_is_norvig(self):
        expected_algorithm = 'norvig'
        self.xml_config.modify_algorithm('norvig')
        current_algorithm = self.xml_config.get_algorithm()
        self.assertEquals(expected_algorithm, current_algorithm)        

    
    ########### END modify_algorithm ##############  


    def tearDown(self):
        shutil.copy2('copy_config.xml', self.xml_config.path_name)
        os.remove('copy_config.xml')

        shutil.copy2('copy_game_settings.xml', self.path_game_settings)
        os.remove('copy_game_settings.xml')
        
        test_output = os.path.abspath("..\\..\\config_test_no_ouput_type.xml")
        if os.path.isfile(test_output):
            os.remove(test_output)

        test_algorithm = os.path.abspath("..\\..\\config_test_no_algorithm.xml")
        if os.path.isfile(test_algorithm):
            os.remove(test_algorithm)

if __name__ == "__main__":
    unittest.main()