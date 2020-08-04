# Author: Jamal Huraibi, fh1328
# Assignment 2
# Question 1
# Python sorted() Doc: docs.python.org/3/library/functions.html#sorted


import statistics                                                               # For .median() and .stddev()


# ----| Functions |--------------------------------------------------------------------------------------------------- #
def write_student_info_to_file(all_students):
    """Writes formatted student information to (file: 'output.txt') """
    file = open("output.txt", "w")                                              # (Open) or (Create + Open) "output.txt"
    student_num = 1                                                             # Used for numbering the output

    file.write("******************\n")                                          # Write section header
    file.write(" Students Records \n")
    file.write("******************\n")
    
    for student in all_students:
        first_name = student[0]                                                 # Intermediate var's for ease of reading
        last_name = student[1]
        average_score = student[2]
        high_score = student[3]
        low_score = student[4]
        letter_grade = student[5]
        
        file.write("{}) {} {}\n".format(student_num, first_name, last_name))    # Write all the student's info
        file.write("Average Score: {}\n".format(average_score))
        file.write("Highest Score: {}\n".format(high_score))
        file.write("Lowest Score: {}\n".format(low_score))
        file.write("Letter grade earned: {}\n".format(letter_grade))
        file.write("\n")                                                        # Write extra space
        
        student_num = student_num + 1                                           # Increment the numbering


def write_class_stats_to_file(all_students):
    """Writes formatted class information to (preexisting file: 'output.txt') """
    file = open("output.txt", "a")                                              # Open "output.txt", in append mode
    num_of_students = len(all_students)
    class_average = calculate_class_average(all_students)
    median_gpa = calculate_median_gpa(all_students)
    std_dev_gpa = calculate_std_dev_gpa(all_students)
    
    file.write("******************\n")                                          # Write section header
    file.write(" Class Statistics \n")
    file.write("******************\n")
    
    file.write("Number of students: {}\n".format(num_of_students))
    file.write("Class Average: {}\n".format(class_average))
    file.write("Median GPA: {}\n".format(median_gpa))
    file.write("Standard deviation: {}\n".format(std_dev_gpa))


def process_raw_line(line_to_process):
    """Removes colon and commas from provided string. Delimits by SPACE and returns as List."""

    # Check if time: Why does replace() work here but not strip() for colon and commas?
    
    processed_line = line_to_process                                            # "line_to_process" is immutable
    
    processed_line = processed_line.replace(':', '')                            # Remove the colon (':')
    processed_line = processed_line.replace(',', '')                            # Remove the commas (',')
    processed_line = processed_line.strip()                                     # Remove trailing artifacts (if exist)
    
    return processed_line.split()                                               # Return as list of individual words


def find_high_score(all_scores):
    """Returns highest score of provided list"""
    high_score = 0.0                                                            # Set initial value
    
    for score in all_scores:
        if float(score) > high_score:                                           # Loop value more than current most?
            high_score = float(score)
    
    return high_score                                                           # Return highest score found


def find_low_score(all_scores):
    """Returns lowest score of provided list"""
    low_score = 100.0                                                           # Set initial value
    
    for score in all_scores:
        if float(score) < low_score:                                            # Loop value less than current least?
            low_score = float(score)
    
    return low_score                                                            # Return lowest score found


# TODO: Value bring printed has large decimal place
def calculate_average_score(all_scores):
    """Returns average score of provided List"""
    scores_subtotal = 0.0
    num_of_scores = len(all_scores)
    
    for score_value in all_scores:
        scores_subtotal += float(score_value)                                   # Sum all the student's scores
    
    return scores_subtotal / num_of_scores                                      # Divide sum by num of scores and return


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


def calculate_class_average(class_students):
    """Returns average score of entire class (all students)"""
    subtotal_score = 0
    num_of_students = len(class_students)
    
    for student in class_students:
        student_avg_score = student[2]
        subtotal_score += student_avg_score                                     # Sum the avg. score of each student
    
    average_class_score = subtotal_score / num_of_students                      # Divide sum by class size and return

    return "%.2f" % average_class_score                                         # Return formatted to 2 decimal places


def calculate_median_gpa(class_students):
    """Returns median score of entire class (all students)"""
    scores = []
    
    for student in class_students:
        scores.append(student[2])                                               # Build a list of all student's scores

    return "%.1f" % statistics.median(scores)                                   # Execute Python's built-in median func.


def calculate_std_dev_gpa(class_students):
    """Returns the standard deviation of entire class' avg scores (all students)"""
    scores = []
    
    for student in class_students:
        scores.append(student[2])                                               # Build a list of all student's scores

    return "%.3f" % statistics.stdev(scores)                                    # Execute Python's built-in stddev func.
    
    
def extract_student_information(data):
    """Returns a List of all the student's information extracted from the string"""
    student_information = []

    first_name = data[0]
    last_name = data[1]
    scores = extract_student_scores(data[2:])                                   # Remaining values should only be scores

    average_score = calculate_average_score(scores)
    high_score = find_high_score(scores)
    low_score = find_low_score(scores)

    letter_grade = convert_to_letter_grade(average_score)
    
    student_information.append(first_name)                                      # Build the List
    student_information.append(last_name)
    student_information.append(average_score)
    student_information.append(high_score)
    student_information.append(low_score)
    student_information.append(letter_grade)
    
    return student_information                                                  # Return built List of student's info


def extract_student_scores(data):
    """Returns a List of the student's scores. "data" should only be scores.
    Checks if each item in data is a number or not also. Appends to "scores" if it is."""
    scores = []
    for value in data:
        try:
            float(value)
            scores.append(value)                                                # Append the number to the List scores
        except ValueError:
            print("[INFO]: Non-number value encountered. Offender: {}\n"        # If float cast fails then not a number
                  .format(value))

    return scores                                                               # Return the built list of scores
    
# ----| main |-------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    students = []                                                               # List of students (will be 2D later)
    fileInStream = open("input.txt", 'r')                                       # Open the in-stream file in read mode
    
    for line in fileInStream:
        currentLine = process_raw_line(line)                                    # Remove unwanted characters

        studentInfo = extract_student_information(currentLine)                  # Build the list of info
        students.append(studentInfo)                                            # Assign the sublist to current index
    
    # Student GPA's: gpa[2] == students[n][2]
    students = sorted(students, key=lambda gpa: gpa[2], reverse=True)           # Sort the list by GPA, descending
    
    write_student_info_to_file(students)                                        # Write each student's info to file
    write_class_stats_to_file(students)                                         # Write class statistics to file

    fileInStream.close()                                                        # Close the stream
    