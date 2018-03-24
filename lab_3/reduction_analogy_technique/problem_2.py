# Solution to Problem 2
# I notice that I can use my solution to Q5 for this problem,
# so I will import it as a module!

import bin_conversion

def rice_survey():
    questions = [
    "Did you use extra nitrogen-based fertiliser? (y/n): ",
    "Did you use extra phosphate-based fertiliser? (y/n): ",
    "Did you allow early flooding of the field? (y/n): ",
    "Was the field left fallow (empty) the previous season? (y/n): ",
    "Did you harvest early? (y/n): ",
    "Did you drain the field before harvest? (y/n): ",
    "Were the grains dried in the sun before delivery? (y/n): ",
    "Did you use the more expensive new variety? (y/n): "]
    treatment_number = ""
    for i in range(len(questions)):
        answer = input(questions[i])

        while answer != "y" and answer != "n":
            print("Please answer y or n.")
            answer = input(questions[i])
        
        if answer == "y":
            treatment_number += "1"
        else:
            treatment_number += "0"

    return bin_conversion.bin_to_dec(treatment_number)

print("\nYour treatment number is", rice_survey())

# returns a list of answers for the questions in order
def survey_answers():
    answers = []
    treatment_number = int(input("Treatment number: "))
    # I wrote another method in bin_conversion.py to convert the treatment_number to binary
    treatment_number = bin_conversion.dec_to_bin(treatment_number)

    for i in list(treatment_number):
        if i == "1":
            answers.append("y")
        else:
            answers.append("n")

    return answers

print(survey_answers())
