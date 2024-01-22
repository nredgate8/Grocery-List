#Audrey Young and Norah Redgate 
#Individual for options 5, 6, and 7
#1/11/2024 and 1/18/2024
#To-Do List

#Function
grocerylist = []
def additem():#Adds item to the list
    addeditem = input("What item do you want to add? ")
    grocerylist.append(addeditem)
    print(grocerylist)

def viewlist():#Prints the current items in the list
    print(grocerylist)

def completedtask():#Marks an item as purchased
    finishedtask = input("Which item did you purchase? ")
    position = int(input("What position is this item in? "))
    finishedtask = "X " + finishedtask
    grocerylist.pop(position)
    grocerylist.insert(position, finishedtask)
    print(grocerylist)

def removetask(): #Removes an item from the list
    position2 = int(input("Which position is the item you want to remove in? "))
    grocerylist.pop(position2)
    print(grocerylist)

def clearlist(): #Allows users to Clear the entire list of notes. This operation is useful for starting fresh or when the user wants to delete all notes at once.
    grocerylist.clear()
    print(grocerylist)

def alphabetical(): #Allows the user to sort their list alphabetically
    grocerylist.sort()
    print(grocerylist)

def printnumber():
    length = len(grocerylist)
    print(length)

def finallist(): #Combines all of the functions to create a custom grocery list
    print("Welcome to your Grocery List: Pick and option 1-5")
    print("1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list \n5. Removes all items from the list  \n6. Sort the list alphabetically \n7. Print the number of items on the list \n8. Exit the program")
    option = int(input("Option: ")) 
    if (option == 1):
        additem()
    if (option == 2):
        viewlist()
    if (option == 3):
        completedtask()
    if (option == 4):
        removetask()
    if (option == 5):
        clearlist()
    if (option == 6):
        alphabetical()
    if (option == 7):
        printnumber()
    if (option == 8):
        quit()
    if (option < 1):
        print("Can't be completed")
    if (option > 8):
        print("Can't be completed")
    again = input("Would you like to keep editing? ")
    if (again == "yes"):
        finallist()
    else:
        quit()
    
# Main
finallist()
