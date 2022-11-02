from PyInquirer import prompt, Separator
import csv


# Add user in the spender choice, the first line of the csv file must be equal to 'name' (without quotes)
userList = [Separator('= Spender List =')]

input_file = csv.DictReader(open("users.csv"))
for row in input_file:
   # print(row)
    userList.append(row)

print(userList)
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
        'name': 'name',
        'choices': userList,
        'validate': lambda answer: 'You must choose at least one topping.'
        if len(answer) == 0 else True
    }

]


def new_expense(*args):
    infos = prompt(expense_questions)
    numberSpenders = len(infos['name'])
    equallySpent = int(infos['amount']) / numberSpenders
    # for name in infos['name']:
    #     print(name)
    #     print(equallySpent)
    # Writing the informations on external file
    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for name in infos['name']:
            spamwriter.writerow(
                [equallySpent, infos['label'], name])

    print("Expense Added ! " + str(infos))
    return True
