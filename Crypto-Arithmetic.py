from itertools import permutations

# Function to solve the crypto-arithmetic problem
def crypto_arithmetic():
    # Words involved in the equation
    words = ["SEND", "MORE", "MONEY"]
    
    # Extract unique letters from the words
    unique_letters = set("".join(words))
    if len(unique_letters) > 10:
        raise ValueError("Too many unique letters for digits (max 10 digits).")
    
    # Generate all possible digit assignments (0-9) for these letters
    for perm in permutations(range(10), len(unique_letters)):
        # Create a mapping from letters to digits
        letter_to_digit = dict(zip(unique_letters, perm))
        
        # Convert each word into a number based on the current mapping
        send = int("".join(str(letter_to_digit[letter]) for letter in "SEND"))
        more = int("".join(str(letter_to_digit[letter]) for letter in "MORE"))
        money = int("".join(str(letter_to_digit[letter]) for letter in "MONEY"))
        
        # Check if the equation SEND + MORE = MONEY holds true
        if send + more == money:
            print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
            print(f"Mapping: {letter_to_digit}")
            return
    
    # If no solution was found
    print("No solution found.")

# Run the program
crypto_arithmetic()