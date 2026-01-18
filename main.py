# A Personal project to track my Habits and maintain a Routine.
from models import *
#Main Menu
def main_menu():
    """Display the main menu"""
    print("Habit Tracker")

def loop():
    """Main loop"""
    main_menu()
    print("add_habit | lst | show_streaks | quit")
    line = input(">>>")
    words= line.split(' ')
    command, args = words[0],words[1:]
    while command != "quit":
        key = command.split()
        match key[0]:

            case "add_habit":
                print("Added Habit")
                habit_name = input("Enter habit name: ")
                habit_date = input("Enter date (DD-MM-YYYY): ")
                new = Habit(habit_name, habit_date)
                _agent.append(new)


            case "lst":
                print("Listed Habits")
                for habit in _agent:
                    print(f"{habit.habit} on {habit.date}")

            case "show_streaks":
                print("Your streaks")
                streak=0
                for habit in _agent:
                    if habit==_agent:
                        streak+=1
                        print(f"{habit}= {streak} days")

        print("add_habit | lst | show_streaks | quit")
        line = input('>> ')  # displays a command-line prompter for users to enter command script
        words = line.split(' ')  # separates the command from the script arguments
        command, args = words[0], words[1:]  # command is one of the interpreter script commands outlined in the help above

if __name__ == "__main__":
    _agent = []
    loop()


