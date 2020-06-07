# Author: Jamal Huraibi, fh1328
# Assignment 2
# Question 1
from os.path import exists


class FileHelper:
    def __init__(self):
        self.file = None

    def write_to_file(self, data):
        import os
        file_exists = os.path.exists("output.text")
        
        #if file_exists:
        
        
class StudentScores:
    def __init__(self):
        self.studentName = None
        self.studentsScores = None
    
    @staticmethod
    def __letter_grade_from_score(score):
        # CHECK: add error checking for greater than 100 and negative?
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'E'
        else:
            return 'F'
    
    # @staticmethod
    # def __check_output_file_exists:
    
    def read_input_file(self):
        return
    
    # def calculate_average_score:
    #   for each student
    #   for each score


class ClassStatistics:
    def __init__(self):
        self.numOfStudents = None
        self.averageScore = None
        self.medianGrade = None
        self.stdDeviation = None
        self.allScores = None


if __name__ == '__main__':
    file = open("input.txt", 'r')           # Read file and store to local var
    
    #for line in file:
    
