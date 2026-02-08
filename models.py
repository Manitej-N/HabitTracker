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

def streak(habit):
    """Streak habit from habit"""
    global streaks
    streaks += 1



habit1 = Habit('reading', '2025-05-05')
habit2 = Habit('writing', '2025-05-06')
habit3 = Habit('writing', '2025-05-07')

