class CourseTime:
    def __init__(self, day, time):
        self.day = day
        self.time = time

    def getDayName(self):
        if self.day == 1: return "Monday"
        elif self.day == 2: return "Tuesday"
        elif self.day == 3: return "Wednesday"
        elif self.day == 4: return "Thursday"
        elif self.day == 5: return "Friday"
        elif self.day == 6: return "Saturday"
        elif self.day == 7: return "Sunday"
