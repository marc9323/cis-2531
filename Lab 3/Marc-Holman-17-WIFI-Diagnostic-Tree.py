"""
Marc D. Holman
9 / 9 / 2019
CIS 2531 Introduction To Python Programming
Lab 3:  WI-FI Diagnostic Tree
"""

# define some constants
SUCCESS = "Great! Exiting program..."
DID_IT_FIX = "Did that fix the problem?"

# initial output, welcome
print("Welcome to WIFI Diagnostic Program:")
print("Start by rebooting the computer and try to connect again.")

# get user input
userInput = input("Did that fix the problem?")

# enter diagnostic tree
if userInput == 'y':
    print("Great! Exiting program...")
else:
    if userInput == 'n':
        print("Reboot the router and try to connect.")
        userInput = input(DID_IT_FIX)
        if userInput == 'y':
            print(SUCCESS)
        else:
            print("Be sure the cables are plugged in.")
            userInput = input(DID_IT_FIX)
            if userInput == 'y':
                 print(SUCCESS)
            else:
                print("Move the router to a new location and try to connect.")
                userInput = input(DID_IT_FIX)
                if userInput == 'y':
                    print(SUCCESS)
                else:
                    print("Sorry, you'll have to get a new router.")


"""
SAMPLE OUTPUT 1: All no conditions

Welcome to WIFI Diagnostic Program:
Start by rebooting the computer and try to connect again.
Did that fix the problem?n
Reboot the router and try to connect.
Did that fix the problem?n
Be sure the cables are plugged in.
Did that fix the problem?n
Move the router to a new location and try to connect.
Did that fix the problem?n
Sorry, you'll have to get a new router.

SAMPLE OUTPUT 2:  A success condition

Welcome to WIFI Diagnostic Program:
Start by rebooting the computer and try to connect again.
Did that fix the problem?n
Reboot the router and try to connect.
Did that fix the problem?n
Be sure the cables are plugged in.
Did that fix the problem?n
Move the router to a new location and try to connect.
Did that fix the problem?y
Great! Exiting program...

"""
                



    
          
        
        
