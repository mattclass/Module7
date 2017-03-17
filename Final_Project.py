'''
Includes a function that takes at least two user arguments from the command line
25.0 pts
**COMPLETE

Contains at least one if/else statement or uses pandas filtering syntax
25.0 pts
**COMPLETE - Pandas


Performs a calculation on a list or on a pandas column
25.0 pts
**COMPLETE - line 109-126...this calculates what percentage of voters in
the county have the same first name as the user argument name.

Uses at least one dictionary or pandas dataframe
25.0 pts
**COMPLETE - panda dataframes

Has a try/except statement for every function
25.0 pts
**COMPLETE - try/except when checking for the path fo the csv file.

Outputs results to a file, and results are formatted nicely
25.0 pts
**COMPLETE - Outputs to a file.  Formated ok.

Must include a docstring telling us how to run the script
25.0 pts
**COMPLETE - lots to read that note code

Either contains a class to hold related functions, or outputs a simple graph
25.0 pts
**COMPLETE - uses a class early against the user arguments
'''

'''

What do you need to do?
....load this program:  "Langa_Final_Project.py" in a folder.
....save the "monongalia_voter.csv" file in the SAME folder as this program
....enter 2 FIRST names as user arguments when you launch the program in this format:
            "python3 Langa_Final_Project.py FirstName1 FirstName2"
            i.e.: "python3 Langa_Final_Project.py Matt Shari"
....here's what happens:


....what the program does....
It tells you all the first names of the voters in Monongalia County (WV) and how
  how many times that first name occurs.
It takes the two first names you provided and puts them throug a class.
It takes the 1st of the names your entered and shows how many times that first name appears in the Voter Roll
It calculates and tells you what percentage of voters have that same first name.
It tells you the top twenty First names which recur and how often.
It outputs that Top Twenty List to a txt file on your computer.

what it does by section:
1) Imports the necessary modules. (line 79-81)
2)Accepts the User Arguments provided when the program is started. (93-96)
3) Capitalizes in the user arguments to commonness with the csv. (98-100)
4)Runs the user arguments through a Class (112-118)
5)Import the Voter Rolls of Monongalia Country, WV from a csv file on your computer
   and confirms they work with a try/except (126-130)
6) Uses Panda and dataframe to sort and calculate relavent info (133-155)
7) It  starts to print and give you information:
    all the first names in the country voter roll and how often one of the
    entered names shows up.  (158-165)
8) It prints the Top Twenty First names in the voter roll and
    outputs that list to your computer as a txt file.  (169-184)


The csv file is the 2014 Voter Rolls of Monongalia County (West Virginia).
'''





#IMPORT MODULES THAT ARE USED THROUGHOUT
import sys
import pandas as pd
#import matplotlib.pyplot as plt



#TAKE ARGUMENTS FROM THE USER ON THE COMMAND LINE
#Using the sys module, I can accept arguments from the command execution line.
#That's the line that tells the Terminal to execute a specific python program.
#but with this module in the program, I can also let the person executing the
#program input some values at this same stage to get things going faster.


#THESE ARE THE ACTUAL CODES NEEDED FOR THE ASSIGNMENT
user_arg1 = sys.argv[1]
user_arg2 = sys.argv[2]
#user_arg3 = sys.argv[3]

#CONVERT THE USER ARGUMENT IN TO ALL CAPITAL LETTERS TO MATCH THE CSV FILE
user_arg1 = user_arg1.upper()
user_arg2 = user_arg2.upper()

'''
#THESE ARE THE ARGUMENTS TO BE USED WHEN TESTING WITHIN PYCHARM
user_arg1 = 'SHARI'
user_arg2 = 'MATT'

print(user_arg1)
print(user_arg2)
#print(user_arg3)
'''

class Namecharacteristics():

    def __init__(self, name):
        print("Your user input name, {}, loaded successfully. ".format(name))

Name1 = Namecharacteristics(name=user_arg1)
Name2 = Namecharacteristics(name=user_arg2)



#back up path for testing purposes
#path = "/Users/matt/mattpython/practice_programs/FinalProject/monongalia_voters.csv"


path = "monongalia_voters.csv"
try:
    monongalia_voters = pd.read_csv(path)
except IOError:
    print("We cannot find the file.  Please ensure it is in the save folder as the program.")


#HOW MANY VOTERS HAVE THE SAME NAME AS THE USER ARGUMENTS
#this is a dataframe
party_count_df = monongalia_voters['party'].value_counts()
#this is a variable
party_count = party_count_df[0]

#three dataframes
match_df = monongalia_voters[['first', 'last', 'party']]
user_arg1match_df = match_df[match_df['first']== user_arg1]
user_arg1count_df = user_arg1match_df['first'].value_counts()
#test print statements
#print(user_arg1count_df)
#print(user_arg1count_df[0])

#this is a variable
user_arg1count = user_arg1count_df[0]
#test print statement
#print(user_arg1count)

#calculate the average as a percentage
user_arg1_average = float((user_arg1count / party_count) * 100)
#test print statement
#print(user_arg1_average)


input('Press ENTER and I will show you the first names and '
      'how frequently they appear in Monongalia County...')
firstnamecount_df = match_df['first'].value_counts()
print(firstnamecount_df)
input('Press ENTER and I will show you what percent of the voters share the name '
      'of your entered value...')
print('{} is the first name of {} percent of the voters in Monongalia County and {} others have that name.'.format(
    user_arg1, user_arg1_average, user_arg1count))



#PRINT THE TOP TWENTY NAMES IN THE COUNTY AND
#SHOW THAT IN A BAR CHART
input("Press ENTER and we'll show the Top 20 names of voters in "
      "Monongalia County.")
top_twenty_names_df = firstnamecount_df.head(20)
print(top_twenty_names_df)
print("We have also saved a txt file in your folder collecting the Top Twenty Names"
      " It is titled Top_Twenty_Name.txt")

#PLOT THE CHART
#firstnamecount_df['first'].value_counts().plot(kind="bar")
#top_twenty_names_df['first'].value_counts().plot(kind="bar")


#OUTPUT TO A CSV FILE
top_twenty_names_df.to_csv('Top_Twenty_Names.txt', sep='\t',header='first')