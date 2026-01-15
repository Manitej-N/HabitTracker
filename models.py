# This .py file contains all the classes, methods and funtions required for my HabitTracker

class Habit:
    """Habit tracker class"""
    def __init__(self, habit, date):
        """Initialize the Habit class"""
        self.habit = habit
        self.date = date
        self.list = self.agent = []

    class HabitAgent:
        """This is the documentation for HabitAgent.Should Complete the docstring for this class."""

        def __init__(self):  # DO NOT CHANGE
            self.agent = []


    def add_habits(self):
        """Add the habits to the list"""


    def list_habits(self):
        """List all habits"""


    def streak(self):
        "Used to track the streaks of a habit"
        pass




habit1 = Habit('read', '17/5/25')
habit2 = Habit('write', '18/6/25')
habit1.list_habits()
habit2.list_habits()