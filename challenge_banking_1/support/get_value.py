def get_value(transaction):

    word = "deposit" if transaction == 1 else "withdraw"

    try:

        value = float(input(f"Enter the ammount to {word}."))
        
    except ValueError:

        print(f"""
Invalid input. Please enter a number.
""")
        
    return value