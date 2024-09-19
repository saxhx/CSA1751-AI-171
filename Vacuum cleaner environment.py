# Define the vacuum cleaner environment
class VacuumCleanerEnvironment:
    def __init__(self, room_A_dirty, room_B_dirty):
        # Initialize the state of rooms and vacuum position
        self.room_A_dirty = room_A_dirty
        self.room_B_dirty = room_B_dirty
        self.vacuum_position = 'A'  # Start the vacuum cleaner at room A

    # Function to simulate the cleaning process
    def start_cleaning(self):
        print(f"Initial State: Room A: {'Dirty' if self.room_A_dirty else 'Clean'}, Room B: {'Dirty' if self.room_B_dirty else 'Clean'}")

        steps = 0
        while self.room_A_dirty or self.room_B_dirty:
            steps += 1
            print(f"Step {steps}: Vacuum is in room {self.vacuum_position}")

            if self.vacuum_position == 'A':
                if self.room_A_dirty:
                    print("Room A is dirty. Cleaning room A.")
                    self.room_A_dirty = False
                else:
                    print("Room A is already clean. Moving to room B.")
                    self.vacuum_position = 'B'
            elif self.vacuum_position == 'B':
                if self.room_B_dirty:
                    print("Room B is dirty. Cleaning room B.")
                    self.room_B_dirty = False
                else:
                    print("Room B is already clean. Moving to room A.")
                    self.vacuum_position = 'A'

        print(f"Final State: Room A: Clean, Room B: Clean")
        print(f"Cleaning completed in {steps} steps.")

# Test the vacuum cleaner environment
if __name__ == "__main__":
    # Create an environment where both rooms are dirty
    vacuum_environment = VacuumCleanerEnvironment(room_A_dirty=True, room_B_dirty=True)
    vacuum_environment.start_cleaning()