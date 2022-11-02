from PyInquirer import prompt, Separator
import csv


# Add user in the spender choice, the first line of the csv file must be equal to 'name' (without quotes)
userList = [Separator('= Spender List =')]

input_file = csv.DictReader(open("users.csv"))
for row in input_file:
    userList.append(row)

# Checked the good user for checkbox


def add_checked_user(list, user):

    for spender in list[1:]:
        if user == spender['name']:
            list.remove(spender)
            list.append({'name': spender['name'], 'checked': True})
    return list


expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        'type': 'checkbox',
        'qmark': '💰',
        'message': 'Select users concerned by the expense',
        'name': 'spender',
        'choices': userList,
        'validate': lambda answer: len(answer) == 1 or "Select only one user",
    },
    {
        'type': 'checkbox',
        'qmark': '💰',
        'message': 'Select users concerned by the expense',
        'name': 'otherSpenders',
        'choices': lambda answer: add_checked_user(userList, answer['spender'][0])

    }

]


def new_expense(*args):
    infos = prompt(expense_questions)
    # numberSpenders = len(infos['name'])
    # equallySpent = int(infos['amount']) / numberSpenders
    # for name in infos['name']:
    #     print(name)
    #     print(equallySpent)
    # Writing the informations on external file
    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            [infos['amount'], infos['label'], infos['spender'][0], ';'.join(infos['otherSpenders'])])

    print("Expense Added ! " + str(infos))
    return True
