import printbook as pb
import test as database

#Str Variables
str_input = ""
str_name = ""
str_delete = ""

#Booleans for loops
bool_loop = True
bool_delete = True
bool_book_loop = True
bool_main_loop = True

def updateData(str_name):
    """
    Update the data from a element in the table
    """

    print("\n  Which info do you dant to update?\n")
    print("    [F]irst name")
    print("    [L]ast name")
    print("    [C]ellphone")
    print("    [E]mail")
    print("    [N]ote\n")

    str_data = str(input()).lower().strip()

    if str_data == 'f' or str_data == 'first':

        str_new = str(input("New name: "))
        database.editData(str_name, str_data, str_new)
        contactBook()

    elif str_data == 'l' or str_data == 'last':

        str_lname = str(input("New last Name: "))
        database.editData(str_name, str_data, str_lname)
        contactBook()

    elif str_data == 'c' or str_data == 'cellphone':

        str_cell = str(input("New cellphone: "))
        database.editData(str_name, str_data, str_cell)
        contactBook()

    elif str_data == 'e' or str_data == 'email':

        str_email = str(input("New email: "))
        database.editData(str_name, str_data, str_email)
        contactBook()

    elif str_data == 'n' or str_data == 'note':

        str_note = str(input("New note: "))
        database.editData(str_name, str_data, str_note)
        contactBook()

    #database.editData(str_name)

def viewContact():
    """
    View all of the information from a contact
    """

    bool_loop = True

    while bool_loop:
        print("\nWhich contact do you want to view?\nWrite it's first name\n")
        str_name = str(input())

        print("\n    Full Contact: \n")

        database.viewFullContact(str_name)

        print("")

        print("    [U]pdate info")
        print("    [B]ack\n")

        str_input = str(input())

        if str_input == 'u' or str_input == 'update':

            updateData(str_name)
            bool_loop = False

        elif str_input == 'b' or str_input == 'back':

            contactBook()
            bool_loop = False

def deleteContact():
    """
    Delete all of the information from a contact
    """

    bool_delete = True

    print("\nWhich contact do you want to delete?")
    print("Write it's first name\n")
    str_name = str(input())

    print("Are you sure you want to delete %s from your contacts?\n" %(str_name))
    print("    [Y]es")
    print("    [N]o\n")

    while bool_delete:
        str_delete = str(input()).lower().strip()

        if str_delete == 'y' or str_delete == 'yes':
            database.deleteData(str_name)
            bool_delete = False
        if str_delete == 'n' or str_delete == 'no':
            bool_delete = False

def contactBook():
    """
    View a simple list of the contacts showing just their names and last names
    """
    bool_book_loop = True

    print("\n")
    print("    *** My Contacts ***\n")

    database.showContacts()

    print("")
    print("        [A]dd new")
    print("        [V]iew full contact")
    print("        [D]elete contact")
    print("        [B]ack")

    while bool_book_loop:
        str_input = str(input()).lower().strip()

        if str_input == 'a' or str_input == "add":

            database.addData()
            contactBook()
            bool_book_loop = False

        elif str_input == 'v' or str_input == 'view':

            viewContact()
            bool_book_loop = False

        elif str_input == 'd' or str_input == 'delete':

            deleteContact()
            contactBook()
            bool_book_loop = False

        elif str_input == 'b' or str_input == 'back':

            mainMenu()
            bool_book_loop = False


def mainMenu():
    """
    The main menu with the giant book cover
    """
    bool_main_loop = True

    pb.book()

    while bool_main_loop:
        str_input = str(input()).lower().strip()

        if str_input == "o" or str_input == "open":

            contactBook()
            bool_main_loop = False

        elif str_input == "e" or str_input == "exit":

            print("\nHave a nice day!")
            bool_main_loop = False

mainMenu()
