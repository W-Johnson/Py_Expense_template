from PyInquirer import prompt
import csv

status_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New user name: ",
        # validate input must not be empty
        "validate": lambda answer: len(answer) > 0 or "Please enter a name",
    }

]


def status():
    dico = {}
    with open('expense_report.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            list = row[0].split(',')
            print(row)

    return
