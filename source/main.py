import sys
#sys.path.append( 'libs/' )
from libs.xml_config import XMLConfig

class Main():
    def __init__(self):
        self.configuration = XMLConfig()
        self.display_main_menu()
         
    def display_main_menu(self):
        print self.logo()
        self.print_dictionary_list(self.main_menu_options())

        while True:   
            try:
                value = raw_input("Please enter a number: ")
                self.main_menu_options()[value]
                break
            except (RuntimeError, TypeError, NameError,KeyError):
              print "Oops!  That was no valid option number.  Try again..."
        self.execute_main_option(value)  
    def logo(self):
        """ Displays the logo on the menu"""

        res = """--------------------------------------
--------------------------------------
              SUDOKU
--------------------------------------
--------------------------------------"""
        return res
    
    def main_menu_options(self):
        """ Displays the main 3 options for the Sudoku """

        options = {'1': '. Configure', '2': '. Solve Sudoku', '3': '. Generate Sudoku', '4': '. Exit'}
        return options

    def conf_menu_options(self):
        """ Displays the configuration options """

        options = {'1': 'Change Output Type', '2': 'Change Level', '3': 'Change Algorithm to solve Sudokus', '4': 'Back Main Menu'}
        return options
    
    def execute_main_option(self, value):
        """ Executes the menu main options 

            Keyword arguments:
            value -- takes one of the four options to select on the main menu
        """

        if (value == "1"):
            self.display_configure_menu()
        if (value == "2"):
            pass
        if (value == "3"):
            pass
        if (value == "4"):
            pass

    def execute_conf_option(self, value):
        """ Executes the configuration options 

            Keyword arguments:
            value -- takes one of the three options for the configure options
        """

        if (value == "1"):
            self.display_output_type_menu()
        if (value == "2"):
            self.display_level_algorithm_menu()
        if (value == "3"):
            self.display_algorithm_menu()
        if (value == "4"):
            self.display_main_menu()     

    def execute_change_level_option(self, value):
        """ Changes the previous complexity level for create or solve the sudoku 

            Keyword arguments:
            value -- takes one of the three options for the complexity level
        """

        if (value == "1"):
            # save Easy level 
            self.save_level("Easy")
            self.display_main_menu()
            
        if (value == "2"):
            # save Mediun level 
            self.save_level("Medium")
            self.display_main_menu()
            
        if (value == "3"):
            # save Hard level
            self.save_level("Hard")
            self.display_main_menu()
            
        if (value == "4"):
            self.display_configure_menu()

    def execute_change_algorithm_option(self, value):
        """ Changes the previous Algorithm used for create or solve the sudoku 

            Keyword arguments:
            value -- takes one of the three options for the Algorithm
        """        
        if (value == "1"):
            # save Norvig algorithm  
            #self.save_algorithm("Norvig")
            #self.display_main_menu()
            pass
        if (value == "2"):
            # save Backtraking algorithm
            #self.save_algorithm("Backtraking")
            #self.display_main_menu()
            pass
        if (value == "3"):
            # save Custom algorithm
            #self.save_algorithm("Custom")
            #self.display_main_menu()
            pass
        if (value == "4"):
            self.display_configure_menu()

    def execute_change_output_option(self, value): 
        """ Changes the output path for the solved the sudoku 

            Keyword arguments:
            value -- takes one of the two options, solved sudoku could be displayed by command line or by XML
        """ 
        if (value == "1"):
            # save display result in console
            print 'Solved sudoku will be displayed by console'
            pass
        if (value == "2"):
            # save display result in file XML add path to folder
            #if 
            pass
        if (value == "3"):
            self.display_configure_menu()
            
    def display_algorithm_menu(self):
        """ Executes the menu for the Algorithm selection 
            
        """ 

        self.print_dictionary_list(self.change_algorithm_menu_options())

        while True:   
            try:
                value = raw_input("Please enter a number: ")
                self.change_algorithm_menu_options()[value]
                break
            except (RuntimeError, TypeError, NameError,KeyError):
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_change_algorithm_option(value)
    
    
    def display_level_algorithm_menu(self):
        """ Executes the menu for the algorithm level selection 
            
        """ 

        self.print_dictionary_list(self.change_level_menu_options())

        while True:   
            try:
                value = raw_input("Please enter a number: ")
                self.change_level_menu_options()[value]
                break
            except (RuntimeError, TypeError, NameError,KeyError):
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_change_level_option(value)

    def display_output_type_menu(self):
        """ Executes options for the output type 
            
        """ 

        self.print_dictionary_list(self.change_output_type_options())

        while True:   
            try:
                value = raw_input("Please enter a number: ")
                self.change_output_type_options()[value]
                break
            except (RuntimeError, TypeError, NameError,KeyError):
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_change_output_option(value)

    def change_output_type_options(self):
        """ Changes the option for the output type 
            
        """

        options = {'1': 'Display result in the console', '2': 'Save the output in a file', '3': 'Back Configuration Menu'}
        return options
    
    def change_algorithm_menu_options(self):
        """ Defines the Algorithm methods for the resolution 
            
        """

        options = {'1': 'Norvig', '2': 'Backtraking', '3': 'Custom', '4': 'Back Configuration Menu'}
        return options
    
    def change_level_menu_options(self):
        """ Defines the complexity levels for the sudoku creation or resolution 
            
        """

        options = {'1': 'Easy', '2': 'Medium', '3': 'Hard', '4': 'Back Configuration Menu'}
        return options
    
    def display_configure_menu(self):
        """ Executes the options for the configuration menu 
            
        """ 

        self.print_dictionary_list(self.conf_menu_options())

        while True:   
            try:
                value = raw_input("Please enter a number: ")
                self.conf_menu_options()[value]
                break
            except (RuntimeError, TypeError, NameError,KeyError):
              print "Oops!  That was no valid option number.  Try again..." 
        self.execute_conf_option(value)


    def print_dictionary_list(self, dictionary):
        """ Prints the dictionary list for each value 
            
        """ 

        for n in range (1, len (dictionary) + 1):
            for key, value in dictionary.iteritems() :
                if str(n) == key:
                    print key, value

    def save_level(self, value):
        """ Saves the new value assigned for the complexity level
            
        """ 
        print value
        print self.configuration.modify_complexity(value)
                         
if __name__ == "__main__":
    t = Main()
    
    
