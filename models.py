# This .py file contains all the classes, methods and funtions required for my HabitTracker

class Habit:
    """Habit tracker class"""
    def __init__(self, habit, date):
        """Initialize the Habit class"""
        self.habit = habit
        self.date = date

    class HabitAgent:
        """<This is the documentation for HabitAgent. Complete the docstring for this class."""

        def __init__(self, habit_data):  # DO NOT CHANGE
            self._agent = self.__gen_agent(habit_data)  # data structure containing Mail objects DO NOT CHANGE

        # Given email_data (string containing each email on a separate line),
        # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
        @classmethod
        def __gen_agent(cls, habit_data):  # DO NOT CHANGE
            """ generates habits data structure
                :ivar: String
                :rtype: list  """
            agent = []
            for e in habit_data:
                msg = e.split('\n')
                agent.append(
                    Habit(msg[0].split(":")[1], msg[1].split(":")[1]))
            return agent

    def add_habits(self):
        """Add the habits to the list"""
        pass

    def list_habits(self):
        """List all habits"""
        print("Listed Habits")
        print(f"{self.habit} on {self.date}")

    def streak(self):
        """Used to track the streaks of a habit"""
        pass


print(Habit.__doc__)

habit1 = Habit('read', '17/5/25')
habit2 = Habit('write', '18/6/25')
habit1.list_habits()
habit2.list_habits()