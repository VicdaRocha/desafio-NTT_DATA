from challenge_banking_1.support.global_variables import balance,deposit_list,withdrawal_list

def statement():

    global balance,deposit_list,withdrawal_list

    print("""

=======STATEMENT=======

Deposits: 
""")

    for index in range(len(deposit_list)):
    
        print(f"{index}:\t\t{deposit_list[index]:.2f}")

    print("""
Withdrawals: 
""")
    
    for index in range(len(withdrawal_list)):
    
        print(f"{index}:\t\t{withdrawal_list[index]:.2f}")

    print(f"""
Balance:\t{balance:.2f}

======================
""")