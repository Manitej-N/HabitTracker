# A Personal project to track my Habits and maintain a Routine.
from models import Habit
#Main Menu
def main_menu():
    """Display the main menu"""
    print("Habit Tracker")
    print("add_habit | lst | quit")

def loop():
    """Main loop"""
    main_menu()
    line = input(">>>")
    words= line.split(' ')
    command, args = words[0],words[1:]
    while command != "quit":
        key = command.split()
        match key[0]:

            case "add_habit":
                print("Added Habit")

                habit_name = input("Enter habit name: ")
                habit_date = input("Enter date (YYYY-MM-DD): ")

                new = Habit(habit_name, habit_date)
                _agent.append(new)

                return new

            case "lst":
                print("Listed Habits")
                for habit in _agent:
                    print(habit)

        line = input('>>> ')  # displays a command-line prompter for users to enter command script
        words = line.split(' ')  # separates the command from the script arguments
        command, args = words[0], words[1:]  # command is one of the interpreter script commands outlined in the help above

if __name__ == "__main__":
    _agent = []
    loop()


