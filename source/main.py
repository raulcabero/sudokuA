import os
import sys
sys.path.append( 'libs/' )
from xml_config import XMLConfig

class Main():

    def __init__(self):
        self.configuration = XMLConfig()
        self.display_main_menu()
         
    def display_main_menu(self):
        """ Displays the Main Menu and validates the entered values for the required options 

            Keyword arguments:
            op_main_menu -- stores the selected value of available options in the Main Menu 
        """

        print self.logo()
        self.print_dictionary_list(self.main_menu_options())

        while True:   
            op_main_menu = raw_input("\nPlease enter a number: ")
            print ''

            if op_main_menu == "1" or op_main_menu == "2" or op_main_menu == "3" or op_main_menu == "4":
                self.main_menu_options()[op_main_menu]
                break
            else: 
              print "Oops!  That was no valid option number.  Try again..."
        self.execute_main_option(op_main_menu) 

    def logo(self):
        """ Displays the logo on the menu"""

        res = """--------------------------------------
--------------------------------------
              SUDOKU A
--------------------------------------
--------------------------------------"""

        return res
    
    def main_menu_options(self):
        """ Defines the 3 available options for the Sudoku Main Menu

            Keyword arguments:
            main_menu_opts -- stores the dictionary of available options for the Main Menu 
        """

        main_menu_opts = {'1': 'Configure', '2': 'Solve Sudoku', '3': 'Generate Sudoku', '4': 'Exit'}
        return main_menu_opts

    def conf_menu_options(self):
        """ Defines the 3 available options for the: "1 . Configure" option 

            Keyword arguments:
            config_opts -- stores the dictionary of available options for the option "1 . Configure"  
        """

        conf_opts = {'1': 'Change Output format', '2': 'Change Level',
                    '3': 'Change Algorithm to use', '4': 'Back'}

        return conf_opts
    
    def execute_main_option(self, op_main_menu):
        """ Executes the Main Menu for the selected option

            Keyword arguments:
            op_main_menu -- takes one of the four options to select on the Main Menu
        """

        if (op_main_menu == "1"):
            self.display_configure_menu()

        if (op_main_menu == "2"):
            print 'Not implemented yet'
            self.display_main_menu()

        if (op_main_menu == "3"):
            print 'Not implemented yet'
            self.display_main_menu()

        if (op_main_menu == "4"):
            print "Good bye!"

    def execute_conf_option(self, conf_opts):
        """ Executes the selected option on the "1 . Configure" option 

            Keyword arguments:
            config_opts -- takes one of the three options available in the "1 . Configure" option 
        """

        if (conf_opts == "1"):
            self.display_output_type_menu()
        if (conf_opts == "2"):
            self.display_level_algorithm_menu()
        if (conf_opts == "3"):
            self.display_algorithm_menu()
        if (conf_opts == "4"):
            self.display_main_menu()     

    def execute_change_level_option(self, level_opts):
        """ Changes the complexity level for create or solve the sudoku 

            Keyword arguments:
            level_opts -- takes one of the three options for the complexity level
        """

        if (level_opts == "1"):
            # save Easy level 
            self.configuration.modify_complexity('Easy')
            self.execute_change_algorithm_option('4')
            
        if (level_opts == "2"):
            # save Medium level 
            self.configuration.modify_complexity('Medium')
            self.execute_change_algorithm_option('4')
            
        if (level_opts == "3"):
            # save Hard level
            self.configuration.modify_complexity('Hard')
            self.execute_change_algorithm_option('4')
            
        if (level_opts == "4"):
            self.execute_change_algorithm_option('4')

    def execute_change_algorithm_option(self, chng_algorit):
        """ Changes the Algorithm used for create or solve the sudoku 

            Keyword arguments:
            chng_algorit -- takes one of the three options for changing the Algorithm to use
        """ 

        if (chng_algorit == "1"):
            # save Norvig algorithm  
            #self.configuration.('Norvig')
            self.execute_change_algorithm_option('4')
            pass

        if (chng_algorit == "2"):
            # save Backtraking algorithm
            #self.configuration.('Backtraking')
            self.execute_change_algorithm_option('4')
            pass

        if (chng_algorit == "3"):
            # save Custom algorithm
            #self.save_algorithm("Custom")
            #self.display_main_menu()
            self.execute_change_algorithm_option('4')
            pass

        if (chng_algorit == "4"):
            self.display_configure_menu()

    def execute_change_output_option(self, output_opts): 
        """ Changes the output format for the solved the sudoku 

            Keyword arguments:
            output_opts -- takes one of the two options, 
                            solved sudoku could be displayed in console, or in a file
        """ 

        if (output_opts == "1"):
            # display solved sudoku in console
            self.configuration.modify_output_type('console')
            self.execute_change_output_option('3')

        if (output_opts == "2"):
            # save solved sudoku in a file            
            self.configuration.modify_output_type('file')                       
            self.execute_change_output_option('3')                
            
        if (output_opts == "3"):
            self.display_configure_menu()
            
    def display_algorithm_menu(self):
        """ Displays/validates the selected options for the option "3 . Change Algorithm to solve sudokus"

            Keyword arguments:
            algorit_opts -- stores the dictionary of available options for the option 
                            "3 . Change Algorithm"
        """ 

        self.print_dictionary_list(self.change_algorithm_menu_options())

        while True:   
            algorit_opts = raw_input("\nPlease enter a number: ")
            print ''

            if algorit_opts == "1" or algorit_opts == "2" or algorit_opts == "3" or algorit_opts == "4":
                self.change_algorithm_menu_options()[algorit_opts]
                break
            else:
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_change_algorithm_option(algorit_opts)    
    
    def display_level_algorithm_menu(self):
        """ Displays and validates the selected options for the option "2 . Change level"

            Keyword arguments:
            level_opts -- stores the dictionary of available options for the option "2 . Change level"
        """ 

        self.print_dictionary_list(self.change_level_menu_options())

        while True:   
            level_opts = raw_input("\nPlease enter a number: ")
            print ''

            if level_opts == "1" or level_opts == "2" or level_opts == "3" or level_opts == "4":
                self.change_level_menu_options()[level_opts]
                break
            else:
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_change_level_option(level_opts)

    def display_output_type_menu(self):
        """ Displays and validates the selected options for the option "1 . Change output format"

            Keyword arguments:
            output_opts -- stores the dictionary of available options for the option "1 . Change output format"
        """ 

        self.print_dictionary_list(self.change_output_type_options())

        while True:   
            output_opts = raw_input("\nPlease enter a number: ")
            print ''

            if output_opts == "1" or output_opts == "2" or output_opts == "3":
                self.change_output_type_options()[output_opts]
                break
            else:
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_change_output_option(output_opts)

    def change_output_type_options(self):
        """ Defines the 3 available options for the option "1 . Change output format"

            Keyword arguments:
            output_opts -- stores the dictionary of available options for the "1 . Change output format"
        """

        output_opts = {'1': 'Display result in console', '2': 'Save result in a file', '3': 'Back'}    

        return output_opts
    
    def change_algorithm_menu_options(self):
        """ Defines the available Algorithm methods for the sudoku resolution

            Keyword arguments:
            algorit_opts -- stores the selected value for the available Algorithms to use             
        """

        algorit_opts = {'1': 'Norvig', '2': 'Backtraking', '3': 'Custom', '4': 'Back'}
        return algorit_opts
    
    def change_level_menu_options(self):
        """ Defines the available levels for the option "2 . Change level"

            Keyword arguments:
            level_opts -- stores the dictionary of avilable levels for the "2 . Change level"            
        """

        level_opts = {'1': 'Easy', '2': 'Medium', '3': 'Hard', '4': 'Back'}
        return level_opts
    
    def display_configure_menu(self):
        """ Displays and validates the selected options for the option "1 . Configure"

            Keyword arguments:
            config_opts -- stores the dictionary of avilable options for the option "1 . Configure"
        """ 

        self.print_dictionary_list(self.conf_menu_options())

        while True:   
            config_opts = raw_input("\nPlease enter a number: ")
            print ''

            if config_opts == "1" or config_opts == "2" or config_opts == "3" or config_opts == "4":
                self.conf_menu_options()[config_opts]
                break
            else:
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_conf_option(config_opts)


    def print_dictionary_list(self, dictionary):
        """ Prints the dictionary list for each value 
            
        """ 

        for n in range (1, len (dictionary) + 1):
            for key, value in dictionary.iteritems() :
                if str(n) == key:
                    print key, value
                         
if __name__ == "__main__":
    t = Main()