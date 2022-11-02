from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New user name: ",
        # validate input must not be empty
        "validate": lambda answer: len(answer) > 0 or "Please enter a name",
    }

]


def add_user():
    # this function add a new user
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            [infos['name']])
    print("User " + str(infos['name']) + " Added ! ")
    return
