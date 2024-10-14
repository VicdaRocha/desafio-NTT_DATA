from challenge_banking_1.support.global_variables import balance, withdrawal_list, daily_withdrawals, MIN_WITHDRAWAL, MAX_WITHDRAWAL

def withdraw(value):

    global balance, withdrawal_list, daily_withdrawals, MIN_WITHDRAWAL, MAX_WITHDRAWAL

    if daily_withdrawals > 0:

        if not MIN_WITHDRAWAL <= value <= MAX_WITHDRAWAL:

            print("""
Transaction Declined.""")

            if value < MIN_WITHDRAWAL:
                
                print("""Invalid Ammount.
                      """)

            else:
            
                print("""Ammount exceeds withdrawal limit.
                      """)

        else :

            balance -= value
            withdrawal_list.append(value)
            daily_withdrawals -= 1

            print(f"""
Ammount Dispensed.

Receipt Confirmation:
Withdrawal:\t${value:.2f}
New Balance:\t${balance:.2f}

You can still perform {daily_withdrawals} withdrawals today.
""")

    else:

        print("""
Daily withdraw limit reached, please come back tomorrow.
""")