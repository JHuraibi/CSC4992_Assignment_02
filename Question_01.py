# Author: Jamal Huraibi, fh1328
# Assignment 2
# Question 1
from os.path import exists


class FileHelper:
    def __init__(self):
        self.file = None
    
    @staticmethod
    def write_to_file(self, data):
        import os
        file_exists = os.path.exists("output.text")
        
        if not file_exists:
            # DONT overwrite
            pass
        

class Student:
    def __init__(self):
        self.scores = student.scores  # list
        self.firstName = student.firstName
        self.lastName = student.lastName
        self.averageScore = None
        self.highScore = None
        self.lowScore = None
        self.letterGrade = None
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def process_scores(self):
        self.highScore = 0  # Redefine for readability
        self.lowScore = 0
        score_sub_total = 0
        number_of_scores = 5  # Number of scores (is constant)
        
        for score in self.scores:
            if score > self.highScore:
                self.highScore = score
            
            if score < self.lowScore:
                self.lowScore = score
            
            score_sub_total += float(score)
        
        self.averageScore = score_sub_total / number_of_scores
    
    def calculate_letter_grade(self):
        score_value = self.averageScore

        if score_value >= 90:
            grade = 'A'
        elif score_value >= 80:
            grade = 'B'
        elif score_value >= 70:
            grade = 'C'
        elif score_value >= 60:
            grade = 'D'
        elif score_value >= 50:
            grade = 'E'
        else:
            grade = 'F'
        
        self.letterGrade = grade


class ClassStatistics:
    def __init__(self):
        self.numOfStudents = None
        self.averageScore = None
        self.medianGrade = None
        self.stdDeviation = None
        self.allScores = None
    
    def add_student(self, student_obj):
        self.add_student(student_obj)


if __name__ == '__main__':
    classStats = ClassStatistics()                                              # Class statistics object
    arr_of_lines = []                                                           # List for each line of the file
    
    file = open("input.txt", 'r')                                               # Open the file in read mode
    
    for line in file:
        currentLine = line                                                      # Local copy of current line of file
        
        currentLine.replace(':', '\0')                                          # Remove the colon (:)
        currentLine.replace(',', '\0')                                          # Remove the commas
        currentLine.split(' ')                                                  # Split line (Delimiter: SPACE ' ')
        
        arr_of_lines.append(line)                                               # Append the processed line to list
    
    for data in arr_of_lines:
        student = Student()
        
        for value in range(0, 5):
            if data == '\n':
                break
            elif nameReadCount == 2:
                student.firstName = data
                nameReadCount -= nameReadCount
            elif nameReadCount == 1:
                student.lastName = data
                nameReadCount -= nameReadCount
            else:
                student.add_score(data)
    
        classStats.add_student(student)                                         # Store the just-built student object
        nameReadCount = 2                                                       # Reset name counter
