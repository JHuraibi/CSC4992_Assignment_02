# Author: Jamal Huraibi, fh1328
# Assignment 2
# Question 1 Add-on

import random

first_names = ["Teresa", "Edith", "Lillie", "Billy", "John", "Grady", "Brittney",
               "Sara", "Dario", "Jody", "Enrique", "Nestor", "Michelle"]

last_names = ["Hinton", "McCoy", "Coffey", "Talent", "Smith", "Carlson", "Barry",
              "Jones", "Harrell", "ODonnell", "Baldwin", "Strickland", "Henry"]


def randomize_names():
    random.shuffle(first_names)
    random.shuffle(last_names)


def write_to_file():
    file = open("input.txt", "w")

    for i in range(13):
        file.write(first_names[i])
        file.write(" ")
        file.write(last_names[i])
        file.write(": ")

        number_of_scores = random.randint(5, 10)                                    # How many random scores to generate

        for j in range(number_of_scores):
            score = random.randint(490, 1000)
            score = score / 10.0

            file.write(str(score))

            if j < number_of_scores:
                file.write(", ")                                                    # Dont print ", " for last score

        file.write("\n")



if __name__ == '__main__':
    randomize_names()
    write_to_file()
