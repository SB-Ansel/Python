#Jake Madden Comparison of network device configurations script.

import os
import sys
import time #may or may not need this feature

class CMP_5350(object):
    def please_stand_by():#fetch device configuration and store it in a tmp.txt file
        return
    def main_menu(self):
        print("}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
        print("      Create DNS records     ")
        print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
        print("1) Create DNS records")
        print("2) Open DNS zone file")
        print("3) Quit")
        # print("\n")
        try:
            option = int(input("Choose your input: "))
        except ValueError:
            print("#################################################################")
            print("Operation could not succeed, contact network administrator.Error 1", sys.exc_info()[0])
            print("#################################################################")
            return
        return option

    def run_main_option(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                try:
                    print_statements("[host name] IN [Record Type] [10.0.0.13 onwards]")
                    host_name = input("Please input host name: ")
                    print_statements("This option only accepts: [A, CNAME, PTR] records.")
                    record = ["A", "CNAME", "PTR"]
                    record_type = str(input("Please select record type: "))
                    if record_type in record:
                        print('\n', record_type,
                              "Selected")  # needed something to complete the if statement so elif wouldn't put up a fuss.
                    elif record_type not in record:
                        print("Whoah Anon! watcha doin!")
                        print("Unknown record type, exiting....")
                        time.sleep(2)
                        break
                    ip_address = input("Please input IP address: ")
                    if len(ip_address) < 12:
                        print('\n', ip_address, 'selected')
                    else:
                        print_statements("The address you have entered appears to be invalid")
                        time.sleep(3)
                        break
                    print('\n', host_name, 'IN', record_type, ip_address)
                    time.sleep(3)
                    print_statements("Writing to DNS Zone file")
                    f = open("cheese.db",
                             "a")  # A option for appending, this line assumes the file in question is in the relative directory since we've not added a greater file path.
                    f.write(
                        '\n' + host_name + ' ' + 'IN' + ' ' + record_type + ' ' + ip_address)  # Bug, for some reason the return carriage[\r] wont work on my linux machine when tested. However I've found away to bypass this issue using the newline command instead, \n.
                    f.close()
                except ValueError:
                    print("##################################################################")
                    print("Operation could not succeed, contact network administrator.Error 2",
                          sys.exc_info()[0])  # In case of failure, this should give a detailed output of the problem.
                    print("##################################################################")
                    return
            elif choice == 2:
                redirect = str(input("Confirm you want to proceed to DNS zone file? Yes/No: "))
                if redirect == 'Yes' or 'yes' or 'y':  # During actual usage i found it tedious to keep writing Yes much lazier to write y.
                    print_statements("Aye! Aye! Captain, Spinning up warp drives! Prepare for file redirection!")
                    time.sleep(3)
                    os.system(
                        "nano cheese.db")  # Uses the native the os editor, on windows, which this to notepad and file.txt for testing. Probably best to have the python script within the same folder.
                    time.sleep(2)
                    sys.exit(0)
                elif redirect == 'No' or 'no' or 'n':
                    return
            elif choice == 3:
                loop = 0
            else:
                # print(print_statements("Can't help noticing you've entered something other than 1-3, are you intentionally trying to break this script?"))
                print_statements(
                    "Can't help noticing you've entered something other than 1-3, are you intentionally trying to break this script?")
                time.sleep(1)
                print_statements("Returning to Main Menu...")
                time.sleep(2)
        print_statements("Thank you and goodbye Anon!")
        print("#########################################")
        print("Operation succeed. Pass ㋡ " "Error = ", sys.exc_info()[0])
        print("#########################################")
foo = CMP_5350()
foo.run_main_option()