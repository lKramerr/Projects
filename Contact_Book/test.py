import mysql.connector

contactBook = mysql.connector.connect(  host = "localhost",
                                        user = "root",
                                        passwd = "password",
                                        database = "ContactBook")

db = contactBook.cursor()

#db.execute("CREATE TABLE contacts(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),lastname VARCHAR(255), cellphone INT, email VARCHAR(255), note VARCHAR(255))")

def addData():
    """
    Add a new contact to the list
    """
    #Data Input
    str_name = str(input("Name: ")).strip()
    str_lname = str(input("Last Name: ")).strip()
    str_cell = str(input("Cellphone: ")).strip()
    str_email = str(input("Email: ")).strip()
    str_note = str(input("Note: ")).strip()

    sql = "INSERT INTO contacts(name, lastname, cellphone, email, note) VALUES (%s, %s, %s, %s, %s)"
    val = [str_name, str_lname, str_cell, str_email, str_note]

    db.execute(sql, val)

    contactBook.commit()

    #print(db.lastrowid)

def deleteData(str_name):
    """
    Delete a contact from the table
    """

    db.execute("DELETE FROM contacts WHERE name = '%s'" %(str_name))
    contactBook.commit()

def editData(str_name, str_data, str_new):
    """
    Edit the information from a contact on the table
    """

    if str_data == 'f':
        db.execute("UPDATE contacts SET name = '%s' WHERE name = '%s'" %(str_new, str_name))

    elif str_data == 'l':
        db.execute("UPDATE contacts SET lastname = '%s' WHERE name = '%s'" %(str_new, str_name))

    elif str_data == 'c':
        db.execute("UPDATE contacts SET cellphone = '%s' WHERE name = '%s'" %(str_new, str_name))

    elif str_data == 'e':
        db.execute("UPDATE contacts SET email = '%s' WHERE name = '%s'" %(str_new, str_name))

    elif str_data == 'n':
        db.execute("UPDATE contacts SET note = '%s' WHERE name = '%s'" %(str_new, str_name))

    db.execute(sql)
    contactBook.commit()

#Reset the primary Key if a contact is deleted
sql = "ALTER TABLE contacts AUTO_INCREMENT = 1"
db.execute(sql)
contactBook.commit()

def showContacts():
    """
    Display all contacts in the table
    """
    db.execute("SELECT name, lastname FROM contacts")

    all = db.fetchall()

    for n in all:
        print(n)

def viewFullContact(str_name):
    """
    Display all the information about the contact
    """

    print("")
    db.execute("SELECT name, lastname, cellphone, email, note FROM contacts WHERE name = '%s'" %(str_name))

    all = db.fetchall()

    for n in all:
        print(n)

    return str_name
