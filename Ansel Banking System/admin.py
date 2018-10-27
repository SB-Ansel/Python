###################################################################
### Jake Madden Student Project - Ansel Banking System - CMP4266###
###################################################################

#Formatted in accordance with PEP8

from person import Person


class Admin(Person):
    def __init__(self, name, password, full_rights, address=[None, None, None, None]):  # Initialisation, automatically is called when creating an object.
        super().__init__(name, password, address)
        self.full_admin_rights = full_rights

    def has_full_admin_right(self):
        return self.full_admin_rights
