# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Yizhou Yang,08/10/2020,CodeUpdate):
# RRoot,1.1.2030,Created started script
# <YIZHOU YANG>,<08/10/2020>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt","r") #assume file already exist
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("Please Enter a Task: ")
        priority =input("Please Enter its Priority: ")
        dicRow = {"Task":task,"Priority":priority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        for dicRow in lstTable:
            print(dicRow)
        strChoiceDelete = (input("Which task would you like to delete: "))
        if dicRow["Task"] == strChoiceDelete:
            lstTable.remove(dicRow)
            print(strChoiceDelete + "has been deleted.\n")
        else:
            print ("No such task is present. Please try again.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + ',' + row["Priority"].strip() + '\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Have a good day!")
        break  # and Exit the program
