from challenge_banking_1.support.get_value import get_value

from ..operations.deposit import deposit
from ..operations.withdraw import withdraw
from ..operations.statement import statement

def menu():

    selection = ''

    while selection != 0:

        print("""
Select the type of transaction:
[0] Exit
[1] Deposit Money
[2] Withdraw Cash
[3] Print Statement
""")
        
        try:
            
            selection = int(input("Enter your choice: "))

        except ValueError:

            print(f"""
Invalid input. Please enter a number.
""")
            continue

        if selection == 0:

            print(f"""
Exiting the system. Have a nice day!
""")
            break
        
        elif selection == 1:

            deposit(get_value(selection))
        
        elif selection == 2:

            withdraw(get_value(selection))
        
        elif selection == 3:

            statement()

        else:

            print(f"""
Please, select a valid option.
""")