###################################################################
### Jake Madden Student Project - Ansel Banking System - CMP4266###
###################################################################

# Formatted in accordance with PEP8

# Importing Packages#
from appJar import gui
import time
import sys
from customer import Customer
from admin import Admin
from account import Account

customers_list = []
admins_list = []


class BankSystem(object):
    def __init__(self):  # Initialisation, automatically is called when creating an object.
        self.customers_list = []
        self.admins_list = []
        self.load_bank_data()

    def gui(self):  # Initialisation, automatically is called when creating an object.
        # Defining GUI settings including name and dimensions of the GUI window
        app = gui("Ansel - Banking System")
        app.setIcon("Bank.ico")  # sets the icon image for the gui window.
        app.setGeometry("450x250")
        app.setBg("#bababa")
        #app.setTransparency("86")# App Transparency Only accepts percentage values, I had to modify appJars code to the this to work.
        app.setFont("16", font="Arial")
        app.addLabel("title", "Ansel Banking System")  # Adding widgets to appjars window.
        app.setLabelBg("title", "#0017b9")
        app.setLabelFg("title", "white")
        app.addLabelEntry("name")  # Adding labels or entry's to the GUI
        app.addLabelEntry("password")
        app.addButtons(["Login", "Cancel"], self.pressBtn)  # link the buttons to the function called press
        app.setFocus("name")
        return app

    def run(self):
        app = self.gui()
        self.app = app
        app.go()


    def pressBtn(self, btn):
        if btn == "Login":  # Naming convention btn = button
            name = self.app.getEntry("name")
            password = self.app.getEntry("password")
            msg = self.customer_login(name, password)
            print(msg)

        else:
            self.app.infoBox("Ansel Banking System", "Thanks For Stopping By!", parent=None)
            time.sleep(1)
            self.app.stop()

            #######################
            ###END OF GUI ELEMENTS#
            #######################

    def load_bank_data(self):
        customer_1 = Customer("Adam", "1234", ["14", "Wilcot Street", "Bath", "B5 5RT"])
        account_no = 1234
        account_1 = Account(5000.00, account_no)
        customer_1.open_account(account_1)
        self.customers_list.append(customer_1)

        customer_2 = Customer("David", "password", ["60", "Holborn Viaduct", "London", "EC1A 2FD"])
        account_no += 1
        account_2 = Account(3200.00, account_no)
        customer_2.open_account(account_2)
        self.customers_list.append(customer_2)

        customer_3 = Customer("Alice", "MoonLight", ["5", "Cardigan Street", "Birmingham", "B4 7BD"])
        account_no += 1
        account_3 = Account(18000.00, account_no)
        customer_3.open_account(account_3)
        self.customers_list.append(customer_3)

        customer_4 = Customer("Ali", "150A", ["44", "Churchill Way West", "Basingstoke", "RG21 6YR"])
        account_no += 1
        account_4 = Account(40.00, account_no)
        customer_4.open_account(account_4)
        self.customers_list.append(customer_4)

        admin_1 = Admin("Jake", "1441", True, ["12", "London Road", "Birmingham", "B95 7TT"])
        self.admins_list.append(admin_1)

        admin_2 = Admin("Stish", "2222", False, ["47", "Mars Street", "Newcastle", "NE12 6TZ"])
        self.admins_list.append(admin_2)

    def customer_login(self, name, password):
        found_customer = self.search_customers_by_name(name)
        if found_customer == None:
            return ("The customer has not been found!")
        else:
            if (found_customer.check_password(password) == True):
                self.run_customer_options(found_customer)
                self.app.stop()
            else:
                return ("You have input a wrong password")

    def search_customers_by_name(self, customer_name):
        found_customer = None
        for a in self.customers_list:
            name = a.get_name()
            if name == customer_name:
                found_customer = a
                break
        if found_customer == None:
            print("The customer %s does not exist! Try again..." % customer_name)
        return found_customer

    def main_menu(self):
        # General main menu for both admins and customers
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Ansel Bank System")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Admin login")
        print("2) Customer login With GUI")
        print("3) Quit Ansel Bank System")
        print(" ")
        try:
            option = int(input("Choose your option: "))
        except ValueError:
            print("\n----------------------------------------------------------")
            print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])  # Incase of failure
            print("\n----------------------------------------------------------")
            return
        return option

    def run_main_option(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                try:
                    name = str(input("Please input admin name: "))
                    password = input("Please input admin password: ")
                    msg = self.admin_login(name, password)
                    print(msg)
                except ValueError:
                    print("\n----------------------------------------------------------")
                    print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])  # Incase of failure
                    print("\n----------------------------------------------------------")
                    return
            elif choice == 2:
                app.run()# This allows only the customers has access to the front end login page.
            elif choice == 3:
                loop = 0
        print("Thank you for using Ansel banking system!")
        print("\n----------------------------------------------------------")
        print("Operation succeed. Pass ㋡ " "Error =", sys.exc_info()[0])
        print("\n----------------------------------------------------------")

    def transferMoney(self, sender_account, receiver_name, receiver_account_no, amount):
        pass

    def customer_menu(self, customer_name):
        print("Welcome %s : Your transaction options are:" % customer_name)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer money")
        print("2) Other account operations")
        print("3) profile settings")
        print("4) Sign out")
        print(" ")
        try:
            option = int(input("Choose your option: "))
        except ValueError:
            print("\n----------------------------------------------------------")
            print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])#Incase of failure
            print("\n----------------------------------------------------------")
            return
        return option

    def run_customer_options(self, customer):
        account = customer.get_account()
        loop = 1
        while loop == 1:
            choice = self.customer_menu(customer.get_name())
            if choice == 1:
                # transferMoney()
                print("Not implemented")
            elif choice == 2:
                account.run_account_options()
            elif choice == 3:
                customer.run_profile_options()
            elif choice == 4:
                loop = 0#Exits out of the loop, effectively 'Sign out'.
        print("Exit account operations")
        print("\n----------------------------------------------------------")
        print("Operation succeed. Pass ㋡ " "Error =", sys.exc_info()[0])
        print("\n----------------------------------------------------------")

    def admin_login(self, name, password):
        found_admin = self.search_admin_by_name(name)
        if found_admin == None:
            return ("The admin user has not been found!")
        else:
            if (found_admin.check_password(password) == True):
                self.run_admin_options(found_admin)
            else:
                return ("you have input a wrong password")

    def search_admin_by_name(self, admin_name):
        found_admin = None
        for a in self.admins_list:
            name = a.get_name()
            if name == admin_name:
                found_admin = a
                break
        if found_admin == None:
            print("That user %s does not exist! Try again..." % admin_name)#Print out notifying the user that an admin user was not found.
        return found_admin

    def admin_menu(self, admin_name):
        print(" ")
        print("Welcome %s : Available options are:" % admin_name)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer money")
        print("2) Customer account operations")
        print("3) Customer profile settings")
        print("4) Admin profile settings")
        print("5) Delete customer")
        print("6) Print all customers detail")
        print("7) Print singular customer details")
        print("8) Sign Out ")
        print(" ")
        try:
            option = int(input("Choose your option: "))
        except ValueError:
            print("\n----------------------------------------------------------")
            print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])#Incase of failure
            print("\n----------------------------------------------------------")
            return
        return option

    def run_admin_options(self, admin):
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin.get_name())
            if choice == 1:
                pass
                print("Not implemented")
            elif choice == 2:
                try:
                    customer_name = str(input("Please input customer name: "))
                    customer = self.search_customers_by_name(
                        customer_name)  # Checks if the users has inputted a value equal to that of option 2 ( 2 == Withdraw money option)
                except ValueError:
                    print("\n-----------------------------------------------------------")
                    print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])#Incase of failure
                    print("\n-----------------------------------------------------------")
                    return
                if customer != None:
                    account = customer.get_account()
                if account != None:
                    account.run_account_options()
            elif choice == 3:
                try:
                    customer_name = str(input("Please input customer name: "))
                    customer = self.search_customers_by_name(
                        customer_name)# choice gets the balance for the customer entered in
                except ValueError:
                    print("\n----------------------------------------------------------")
                    print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])  # Incase of failure
                    print("\n----------------------------------------------------------")
                    return
                if customer != None:
                    customer.run_profile_options()

            elif choice == 4:
                admin.run_profile_options()# Allows the user to update name and print details.

            elif choice == 5:
                if admin.has_full_admin_right() == True:
                    customer_name = str(input("Please input customer name you want to delete: "))
                    customer_account = self.search_customers_by_name(customer_name)# We're querying the file to find if a customer matches the entered name by admin.
                    if customer_account != None:#IF statement handles whether or not the account exists != means not equal to.
                        self.customers_list.remove(customer_account)
                        print("\n----------------------------------------------------------")
                        print("Operation succeed. Pass ㋡ " "Error =", sys.exc_info()[0])
                        print("\n----------------------------------------------------------")
                else:
                    print("\nOnly administrators with full admin rights can remove a customer from the bank system!\n")

            elif choice == 6:
                self.print_all_accounts_details()  # uses the print all method from person.py to format the account details.
            elif choice == 7:
                self.print_singular_customer_details()
            elif choice == 8:
                loop = 0#Breaks the loop, effectively making this option a 'sign out'.
        print("Exit account operations")#Informs the user that they have successfully signed out correctly.

    def print_all_accounts_details(self):
        i = 0
        for c in self.customers_list:#Loop through the list until there isn't any more values.
            i += 1#Enables automatic increments of number visuals displayed near customer output.
            print(' %d. ' % i, end=' ')
            c.print_details()
            print("\n----------------------------------------------------------")
            print("Operation succeed. Pass ㋡ " "Error =", sys.exc_info()[0])
            print("\n----------------------------------------------------------")

    def print_singular_customer_details(self):
        name_in = input("Name of a customer: ")
        is_found = False
        for x in self.customers_list:
            if (x.get_name() == name_in):
                x.print_details()#Uses the print details method for formatting.
                is_found = True
                print("\n----------------------------------------------------------")
                print("Operation succeed. Pass ㋡ " "Error =", sys.exc_info()[0])
                print("\n----------------------------------------------------------")
        if (is_found == False):
            print("\n----------------------------------------------------------")
            print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])#Incase of failure.
            print("\n----------------------------------------------------------")


app = BankSystem()
app.run_main_option()
