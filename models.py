# This .py file contains all the classes, methods and funtions required for my HabitTracker
from datetime import date

streaks = 0
class Habit:
    """Habit tracker class"""
    def __init__(self, habit, date):
        """Initialize the Habit class"""
        self.habit = habit
        self.date = date
        self.agent = []

class HabitAgent(Habit):
        """This is the documentation for HabitAgent.Should Complete the docstring for this class."""

    def __init__(self, habit, date):  # DO NOT CHANGE
        super().__init__(habit, date)
        self.agent = []

    def add_habits(self):
        """Add the habits to the list"""
        pass

    def list_habits(self):
        """List all habits"""
        pass

    def streak(self):
        "Used to track the streaks of a habit"
        pass




habit1 = Habit('reading', '2025-05-05')
habit2 = Habit('writing', '2025-05-06')
habit3 = Habit('writing', '2025-05-07')

