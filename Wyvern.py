#Jake Madden Comparison of network device configurations script.
#Package list
import sys#Needed for error handling function, retrieves system data.
import os
class programming_module(object):
    def main_menu(self):
        print("================================================")
        print("Wyvern: Python comparison agent | [Version]: 0.1")
        print("================================================")
        print('''        
 _    _                                  
| |  | |                                 
| |  | | _   _ __   __  ___  _ __  _ __  
| |/\| || | | |\ \ / / / _ \| '__|| '_ \ 
\  /\  /| |_| | \ V / |  __/| |   | | | |
 \/  \/  \__, |  \_/   \___||_|   |_| |_|
          __/ |                          
         |___/                           
        ''')
        print("(Wyvern)> ")
        print("\n")

    def main_menu_settings(self):#Responible for running main menu options in a recursive loop.
        While
        choice = self.main_menu()
        if choice == "help":
            print('''Wyvern Commands
                     ===============''')
            print('''
                    Main            Go back to menu.
                    Kill            Task agent to exit to shell.
                    Sysinfo         Task agent to get system information.
                    Version         Task agent to get software version.''')
            return
        elif choice == "Main":
            return

        elif choice == "Kill":
            return

        elif choice == "Sysinfo":
            os.uname()
            return

        #else:
            #print("place holder")
        #error_handling()
        #loop == 0


def please_stand_by(self):#fetch device configuration and store it in a tmp.txt file
    return

def print_statement(string):#Responible for newline handling with numerous print statements.
    print("\n" + string + "\n")

def error_handling(self):#Responible for handling unanticipated user input.
    print("======================================================")
    print("Operation could not succeed. Error ", sys.exc_info()[0])
    print("======================================================")
    return
foo = programming_module()
foo.main_menu_settings()