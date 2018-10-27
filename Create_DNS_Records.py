# Host records must be in this format [host name] IN A [10.0.0.2 onwards]
# CMP - Computer Server Systems - Jake Madden Python script to accomplish elements from questions 1 and complete question 2.
# Packages/Libraries#
import sys
import os
import time
####################
class CMP(object):
    def main_menu(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("     Create DNS A records    ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Manually create DNS records")
        print("2) Open DNS zone file")
        print("3) Quit")
        print(" ")
        try:
            option = int(input("Choose your input: "))
        except ValueError:
            print("###########################################")
            print("Operation could not succeed, contact network administrator. (✖╭╮✖)", sys.exc_info()[0])
            print("############################################")
            return
        return option

    def run_main_option(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                try:
                    print("[host name] IN A [10.0.0.2 onwards]")
                    hostName = input("Please input host name: ")
                    recType = str(input("Please input record type: "))
                    ipAddr = input("Please input IP address: ")
                    print("")
                    print(hostName, 'IN', recType, ipAddr)
                    print("")
                    time.sleep(3)
                    print("")
                    print("Writing to DNS Zone file")
                    print("")
                    f = open("cheese.db", "a") #A option for appending, This assume the file in question is in the relative directory.
                    f.write('\n'+hostName + ' ' + 'IN' + ' ' + recType + ' ' + ipAddr)#Bug, for some reason the return carriage[\r] wont work on my linux machine when tested. I'm using the \n to bypass this issue.
                    f.close()
                except ValueError:
                    print("\n----------------------------------------------------------")
                    print("Operation could not succeed. Error (✖╭╮✖)", sys.exc_info()[0])  # Incase of failure
                    print("\n----------------------------------------------------------")
                    return
            elif choice == 2:
                redirect = str(input("Confirm you want to proceed to DNS zone file? Yes/No: "))
                if redirect == 'Yes':
                    print("")
                    print("Aye! Aye! Captain, Spinning up warp drives!!")
                    print("")
                    time.sleep(3)
                    os.system("nano cheese.db")
                    time.sleep(2)
                    sys.exit(0)
                elif redirect == 'No':
                    return
            elif choice == 3:
                loop = 0
            else:
                print("")
                print("Can't help noticing you've entered something other than 1-4, are you intentionally trying to break this script?")
                time.sleep(2)
                print("Returning to Main Menu...")
                time.sleep(5)
                print("")
                print("")
                print("")
        print("")
        print("Goodbye Anon!")
        print("#########################################")
        print("Operation succeed. Pass ㋡ " "Error = ", sys.exc_info()[0])
        print("#########################################")

foo = CMP()
foo.run_main_option()
