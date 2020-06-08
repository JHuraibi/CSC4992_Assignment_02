# Author: Jamal Huraibi, fh1328
# Assignment 2
# Question 1


# ----| Functions |--------------------------------------------------------------------------------------------------- #

def process_raw_info(line_to_process):
    """Removes colon and commas from (line_to_process: str). Returns list delimited by SPACE(' ')."""
    processed_line = line_to_process                                            # "line_to_process" is immutable
    
    processed_line = processed_line.replace(':', '')                            # Remove the colon (':')
    processed_line = processed_line.replace(",", "")                            # Remove the commas (',')
    
    return processed_line.split()                                               # Return as individual words


def find_high_score(all_scores):
    """Returns highest score within the sublist passed-in"""
    high_score = 0.0
    
    for score in all_scores:
        if score > high_score:
            high_score = score
    
    return high_score


def find_low_score(all_scores):
    """Returns lowest score within the sublist passed-in"""
    low_score = 0.0
    
    for score in all_scores:
        if score < low_score:
            low_score = score
    
    return low_score


def calculate_average_score(all_scores):
    """Returns average score"""
    scores_subtotal = 0
    num_of_scores = len(all_scores)
    
    for score_value in all_scores:
        scores_subtotal += score_value
    
    return scores_subtotal / num_of_scores


def convert_to_letter_grade(score):
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
    
    
# ----| main |-------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    students = []                                                               # List of students
    data = []                                                                   # List for each line of the file
    
    fileInStream = open("input.txt", 'r')                                       # Open the file in read mode
    fileOutStream = open("output.txt", 'w')                                     # (Open) or (Create + Open) "output.txt"
    
    fileOutStream.write("******************")                                   # Write file header
    fileOutStream.write(" Students Records ")
    fileOutStream.write("******************")
    
    for line in fileInStream:
        student = process_raw_info(line)                                        # Remove unwanted characters
        
        firstName = student[0]
        lastName = student[1]
        highScore = find_high_score(student[2:7])
        lowScore = find_low_score(student[2:7])
        avgScore = calculate_average_score(student[2:7])
        letterGrade = convert_to_letter_grade(avgScore)
        
        
