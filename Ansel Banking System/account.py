###################################################################
### Jake Madden Student Project - Ansel Banking System - CMP4266###
###################################################################

import sys #module used for handling errors

class Account:
    def __init__(self, balance, account_no):  # Initialisation, automatically is called when creating an object.
        self.balance = float(balance)
        self.account_no = account_no

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):  # Mirroing the above deposit in format but instead of depositing money we're withdraw, this is done with the (-=)
        self.balance -= amount

    def print_balance(self):
        print("Your account balance is %.2f" % self.balance)

    def get_balance(self):
        return self.balance

    def get_account_no(self):
        return self.account_no

    def account_menu(self):
        print("Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit Money")
        print("2) Withdraw Money")
        print("3) Check balance")
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

    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                    try:
                        amount = float(input("Please enter amount to be deposited: "))
                        self.deposit(amount)
                        self.print_balance()
                    except ValueError:
                        print("\n----------------------------------------------------------")
                        print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])  # Incase of failure
                        print("\n----------------------------------------------------------")
                        return
            elif choice == 2:
                    try:
                        withdrawAmount = float(input("Please enter amount to be withdrawn: "))
                        self.withdraw(withdrawAmount)
                        self.print_balance()
                    except ValueError:
                        print("\n----------------------------------------------------------")
                        print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])  # Incase of failure
                        print("\n----------------------------------------------------------")
                        return
            elif choice == 3:
                # balance = self.print_balance()
                self.print_balance()
            elif choice == 4:
                loop = 0
        print("Exit account operations")
