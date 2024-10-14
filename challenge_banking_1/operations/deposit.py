from challenge_banking_1.support.global_variables import balance, deposit_list, MIN_DEPOSIT

def deposit(value):

    global balance, deposit_list, MIN_DEPOSIT

    if value < MIN_DEPOSIT:

        print("""
You must inform a positive ammount for the deposit.
""")

    else: 

        balance += value
        deposit_list.append(value)
        
        print(f"""
Ammount Deposited.

Receipt Confirmation:
Deposit:\t${value:.2f}
New Balance:\t${balance:.2f}
                """)