from coursetime import CourseTime

class Course:
    def __init__(self, name):
        self.name = name
        self.timeList = []

    def addTime(self, day, time):
        self.timeList.append( CourseTime(day, time) )

    def getDetailName(self):
        string = str(self.name)

##        i = 0
##
##        while i < len(self.timeList):
##            time = self.timeList[i]
##            
##            if i == 1: string = string + str(" (")
##
##            string += str(self.getDayName(time.day)) + str(" ") + str(time.time)
##
##            i += 1
##            
##            if i != len(self.timeList): string += str(", ")

        return string

    def getDayName(self, dayNumber):
        if dayNumber == 1: return "Senin"
        elif dayNumber == 2: return "Selasa"
        elif dayNumber == 3: return "Rabu"
        elif dayNumber == 4: return "Kamis"
        elif dayNumber == 5: return "Jumat"
        elif dayNumber == 6: return "Sabtu"
        elif dayNumber == 7: return "Minggu"
