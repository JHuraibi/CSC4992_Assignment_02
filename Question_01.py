# Author: Jamal Huraibi, fh1328
# Assignment 2
# Question 1


def write_to_file(data_to_write):
    """Prints/Outputs (data_to_write: str) to file (output.txt)"""
    import os
    file_exists = os.path.exists("output.text")
    
    if not file_exists:
        # DONT overwrite
        pass
    else:
        # Overwrite OK
        pass
    

def process_raw_line(line_to_process):
    """Removes colon and commas from (line_to_process: str). Delimits by SPACE(' ')."""
    processed_line = line_to_process

    processed_line.replace(':', '\0')                                          # Remove the colon (:)
    processed_line.replace(',', '\0')                                          # Remove the commas
    processed_line.split(' ')                                                  # Split line (Delimiter: SPACE ' ')
    
    return processed_line


def process_scores(raw_data):
    """Builds a list of scores from (raw_data: str)."""
    number_of_scores = -5
    list_of_scores = []
    
    for index in range(-1, number_of_scores):
        score = raw_data[index]
        list_of_scores.append(score)
        
    return list_of_scores


def calculate_letter_grade(score):
    """Returns the letter grade for (score: float)"""
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    elif score >= 50.0:
        return 'E'
    else:
        return 'F'


if __name__ == '__main__':
    # students(fName, lName, scores[], GPA)
    student_data = []                                                           # List for each line of the file
    indexFName = 0
    indexLName = 1
    indexScores = 2
    indexGPA = 3
    
    file = open("input.txt", 'r')                                               # Open the file in read mode
    
    for line in file:
        # File is opened in "read" mode
        currentLine = process_raw_line(line)                                    # Format the line
        student_data.append(currentLine)                                        # Append the processed line to list
        
    for data in student_data:
        students_scores = process_scores(data)
        print()