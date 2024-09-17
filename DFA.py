class DFA:
    def __init__(self):
        # Initial state
        self.current_state = 'q0'
        # Final (accept) state
        self.accept_state = 'q2'
        # Transition function as a dictionary
        self.transitions = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q1', '1': 'q2'},
            'q2': {'0': 'q1', '1': 'q0'}
        }

    # Method to process the input string
    def process_input(self, input_string):
        for char in input_string:
            if char in self.transitions[self.current_state]:
                self.current_state = self.transitions[self.current_state][char]
            else:
                return False  # Invalid character found
        return self.current_state == self.accept_state

# Sample input and output
dfa = DFA()
input_string = input("Enter a binary string: ")

if dfa.process_input(input_string):
    print(f"String '{input_string}' is accepted.")
else:
    print(f"String '{input_string}' is rejected.")