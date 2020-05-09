from course import Course

class CourseLogic():
    def loadFile(self):
        self.file = open('courses/2d4itb.course', 'r')
        self.lines = self.file.readlines()

    def getCourseList(self):
        courseList = []
        
        indicator = ','
        i = 0
        
        while self.lines[i] != ';':
            line = self.lines[i]
            indexList = self.getIndexInString(line, indicator)

            name = line[ 0 : (indexList[0] - 1) ]

            course = Course(name.strip())

            j = 1

            while j < len(indexList):
                day = int(line[ (indexList[j - 1] + 2) ])
                time = line[ (indexList[j] + 2) : (indexList[j] + 7) ]

                course.addTime(day, time)

                j += 2

            courseList.append(course)

            i += 1
                
        return courseList
            

    def getIndexInString(self, line, indicator):
        indexList = []

        for i, char in enumerate(line):
            if char == indicator:
                indexList.append(i)

        return indexList
