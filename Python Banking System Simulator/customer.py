###################################################################
### Jake Madden Student Project - Ansel Banking System - CMP4266###
###################################################################

#Formatted in accordance with PEP8

from person import Person


class Customer(Person):
    def __init__(self, name, password,
                 address=[None, None, None, None]):  # Initialisation, automatically is called when creating an object.
        super().__init__(name, password, address)

    def open_account(self, account):
        self.account = account

    def get_account(self):
        return self.account

    def print_details(self):
        super().print_details()
        bal = self.account.get_balance()
        print('Account balance: %.2f' % bal)
        print(" ")

    def get_name(self):
        return self.name