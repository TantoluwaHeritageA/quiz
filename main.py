question_bank = {
    'science': {
        'a': {
            'question': 'In what tabular display are the chemical elements typically displayed?',
            'answer': 'Periodic table'
        },

        'b': {
            'question': 'What tissue connects bone to muscle?',
            'answer': 'Tendons'
        },
        'c': {
            'question': 'Anaemia is caused by the deficiency of which mineral in the human diet?',
            'answer': 'Iron'
        },
        'd': {
            'question': 'How is ‘Sound Navigation and Ranging’ more commonly known?',
            'answer': 'Sonar'
        },
        'e': {
            'question': 'At room temperature, what is the normal state of the element Mercury?',
            'answer': 'Liquid'
        },
    },

    'politics': {
        'a': {
            'question': 'Who is the current British head of state?',
            'answer': 'Queen Elizabeth',
        },
        'b': {
            'question': 'What does the acronym MP stands for in politics?',
            'answer': 'Member of Parliament'

        },

        'c': {

            'question': 'Which branch of government is responsible for making laws?',

            'answer': 'Legislative'

        },

        'd': {

            'question': 'What is the lower house of the Parliament of the United Kingdom called?',

            'answer': 'The House of Commons'

        },

        'e': {

            'question': 'When did the concepts of democracy first originate?',

            'answer': 'Ancient Greece'

        },
    }
}


def get_questions():
    choice = input("Enter segment: politics or science, pick one; ")
    if choice in question_bank:
        question_list = question_bank[choice]
        print(question_list)
        print(f'you have chosen {choice} segment, proceed by picking a letter')

    else:
        print("there are two segments;science & politics ")


def ans_questions_science():
    question_list = question_bank['science']
    money_won = 1
    for keys in question_list:
        pick_quest = input('enter a letter: ')
        quest = question_list[keys]['question']
        if pick_quest != keys:
            pass
        else:
            print(quest)
        answer = str(input('Enter an answer: '))
        ans = question_list[keys]['answer']
        attempts = 2
        total = 0

        if answer == ans.lower():
            money_won = money_won * 500
            print(f"You just won € {money_won}")

        else:
            print('wrong')


# end=" "


def ans_questions_politics():
    question_list = question_bank['politics']
    money_won = 1
    for keys in question_list:
        pick_quests = input('enter a letter: ')
        quests = question_list[keys]['question']
        if pick_quests != keys:
            pass
        else:
            print(quests)
        answer = str(input('Enter an answer: '))
        ans = question_list[keys]['answer']
        if answer == ans.lower():
            money_won = money_won * 500
            print(f"You just won € {money_won}")

        else:
            print('wrong')


def check():
    option = get_questions()
    if option == 'science':
        return ans_questions_science()
    else:
        return ans_questions_politics()


check()

# for keys in question_list:
#     choice = input('enter a letter: ')
#     if choice == key:
#         quest = questions[key]['question']
#         ans = questions[key]['answer']
#         print(quest)
#         continue
#         answer = input('enter answer: ')
#         if answer == ans:
#             print('correct')
#         else:
#             print('wrong')
# print(quest + ' - Ans: ' + ans)
# answer
