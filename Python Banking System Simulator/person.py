###################################################################
### Jake Madden Student Project - Ansel Banking System - CMP4266###
###################################################################

#Formatted in accordance with PEP8

import sys #module used for handling errors


class Person(object):
    def __init__(self, name, password,
                 address=[None, None, None, None]):  # Initialisation, automatically is called when creating an object.
        self.name = name
        self.password = password
        self.address = address

    def get_address(self):
        return self.address

    def update_name(self, name):
        self.name = name

    def update_address(self, address):  # Keeping the formatting similar to update_name since this method is doing a similar task.
        self.address = address

    def get_name(self):
        return self.name

    def print_details(self):
        print("Name %s:" % self.name)
        print("Address: %s" % self.address[0])
        print("         %s" % self.address[1])
        print("         %s" % self.address[2])
        print("         %s" % self.address[3])
        print(" ")

    def check_password(self, password):
        if self.password == password:
            return True
        return False

    def profile_settings_menu(self):
        print("Your Profile Settings Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Update Name")
        print("2) Print details")
        print("3) Update Address")
        print("4) Back")
        print(" ")
        try:
            option = int(input("Choose your option: "))
        except ValueError:
                print("\n----------------------------------------------------------")
                print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])  # Incase of failure
                print("\n----------------------------------------------------------")
                return
        return option

    def run_profile_options(self):
        loop = 1
        while loop == 1:
            choice = self.profile_settings_menu()
            if choice == 1:
                    try:
                        name = input("Please enter new name: ")
                        self.update_name(name)
                    except ValueError:
                        print("\n----------------------------------------------------------")
                        print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])#Incase of failure
                        print("\n----------------------------------------------------------")
                        return
            elif choice == 2:
                self.print_details()
            elif choice == 3:
                    try:
                        updateAddress = input("Please enter your updated address, Four parts are accepted, no spaces after the letter of your new address: ")
                        updateAddress = [updateAddress.split() for updateAddress in updateAddress.split(" ",)]#When the user updates their address their input is split and formatted to follow the originals systems design.
                        if (len(updateAddress) != 4):
                            print("\n----------------------------------------------------------")
                            print("Operation could not succeed. Error#1 (✖╭╮✖)", sys.exc_info()[0])#Incase of failure
                            print("\n----------------------------------------------------------")
                        else:
                            self.update_address(updateAddress)
                    except IndexError:
                            print("\n----------------------------------------------------------")
                            print("Operation could not succeed. Error#2 (✖╭╮✖)", sys.exc_info()[0])#Incase of failure
                            print("\n----------------------------------------------------------")
                            return
            elif choice == 4:
                loop = 0
