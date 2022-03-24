from quiz import question_bank


def get_questions():
    choice = input("Enter segment: politics or science, pick one; ")
    if choice == 'politics':
        question_soup = question_bank['politics']
        money_won = 1
        for keys in question_soup:
            quests = question_soup[keys]['question']
            print(quests)
            answer = str(input('Enter an answer: '))
            ans = question_soup[keys]['answer']
            if answer == ans.lower():
                money_won = money_won * 500
                print(f"You just won € {money_won}")
            else:
                print(f"You just lost 100 euros ")
    elif choice == 'science':
        question_soups = question_bank['science']
        money_won = 1
        for key in question_soups:
            quest = question_soups[key]['question']
            print(quest)
            answer = str(input('Enter an answer: '))
            ans = question_soups[key]['answer']
            if answer == ans.lower():
                money_won = money_won * 500
                print(f"You just won € {money_won}")
            else:
                print("incorrect ")
    else:
        print("end")


get_questions()
