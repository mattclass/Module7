'''
Finish walking through this lecture to copy/paste the beginning of the script you will need for your homework. (Links to an external site.)
 - COMPLETE
Finish the user option to delete an entry from the dictionary by removing the "pass" statements and adding code to delete a user by name (extra challenge: can you figure out how to delete a user by name OR username?)
 - COMPLETE
Finish the user option to lookup a username by name by removing the "pass" statement and adding code to find a user by name
 - COMPLETE
Run the script and make sure each option works
 - COMPLETE
Add exception handling to each user input option.
 - COMPLETE
Add doc strings to the script and comment the code.
 - COMPLETE
Push your finished script to your personal, publicly accessible Github repo.
Submit a link to the Github repo containing your script on canvas.

User can delete an entry from the dictionary
25.0 pts
This criterion is linked to a Learning OutcomeUser can lookup a username by name.
25.0 pts
This criterion is linked to a Learning OutcomeEach user option has exception handling.
15.0 pts
This criterion is linked to a Learning OutcomeScript contains helpful doc strings and comments
10.0 pts
This criterion is linked to a Learning OutcomeFinished script successfully uploaded to Github
25.0 pt'''


#I DON'T REMEMBER WHAT SORTEDCONTAINERS DOES BUT HERE WE'RE IMPORTING A MODULE
#WE DOWNLOADED AND INSTALLED THAT ALLOWS US TO SORT DICTIONARIES
from sortedcontainers import SortedDict

#THIS PRINTS THE MENU THE USER WILL WORK FROM.
def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a user_name')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

#print(SortedDict)
#print(usernames)

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
#THIS BEGINS THE IMPLEMENTATION OF EXECUTING WHATEVER THE USER INPUT.
#IT ALSO HAS A COUPLE TRY STATEMENTS WHICH WILL CHECK FOR
#SOME EXCEPTION ERRORS

while menu_choice != 5:
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("\nReally need and integer.  How about we try again.\n\n")

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        try:
            name = input("Name: ")
# I TRIED TO BE CLEVER HERE AND PROVIDE THE USER WITH CONFIRMATION THAT THE
# DELETE ACTUALLY OCCURED.  BUT FOR SOME REASON, THESE PRINT STATEMENTS
# EXECUTED EVEN WHEN THE try STATEMENT FAILED.
#            print("We just deleted {} from the dictionary.  "
#                  "Go ahead.  Hit 1 to see.".format(name))
#  WHY DOES a bad entry print the print statements above AND jump to the except.
            del usernames[name]
        except KeyError:
            print('That name does not appear in the list.  Please note it is case-sensitive.')
#            if name in usernames:
#              del usernames[name] # delete that entry


    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            input('This is super secret.  Please install your privacy screen.  Press Enter when the coast is clear...')
            print(usernames.get(name))# print the username
        else:
            print('Whoa buddy...that person is not in our dictionary.'
                  '  Are you sure you are not on some espionage mission to steal usernames?!')  # print username not found

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()
