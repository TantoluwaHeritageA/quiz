from quiz import question_bank

choice = input("Enter segment: politics,geography or science, pick one; ")


def get_questions_science():
    if choice == 'science':
        question_soups = question_bank['science']
        money_won = 500
        for key in question_soups:
            quest = question_soups[key]['question']
            print(quest)
            count = 0
            attempt = 2
            ans = question_soups[key]['answer']
            while attempt > 0:
                answer = str(input('Enter an answer: '))
                if answer == ans.lower():
                    money_won = money_won + 500
                    print(f"You just won € {money_won}")
                    break
                else:
                    attempt = attempt - 1
                    # money_won = money_won - 100
                    print(
                        f"you have {attempt} attempt ,, try again \n Your new balance is {money_won} euros")
                    exit
    else:
        pass


def get_questions_politics():
    if choice == 'politics':
        question_soup = question_bank['politics']
        money_won = 500
        for keys in question_soup:
            quests = question_soup[keys]['question']
            print(quests)
            attempts = 2
            ans = question_soup[keys]['answer']
            while attempts > 0:
                answer = str(input('Enter an answer: '))
                if answer == ans.lower():
                    money_won = money_won + 500
                    print(f"You just won € {money_won}")
                    break
                else:
                    attempts = attempts - 1
                    # money_won = money_won - 100
                    print(
                        f"you have {attempts} attempt ,, try again \n Your new balance is {money_won} euros")
                    exit
    else:
        pass


def get_questions_geog():
    # choice = input("Enter segment: politics or science, pick one; ")
    if choice == 'geography':
        question_soupy = question_bank['geography']
        money_won = 500
        for keys in question_soupy:
            quests = question_soupy[keys]['question']
            print(quests)
            ans = question_soupy[keys]['answer']
            attempt = 2
            while attempt > 0:
                answer = str(input('Enter an answer: '))
                if answer == ans.lower():
                    money_won = money_won + 500
                    print(f"You just won € {money_won}")
                    break
                else:
                    attempt = attempt - 1
                    # money_won = money_won - 1
                    print(
                        f"you have {attempt} attempt ,, try again \n Your new balance is {money_won} euros")
                    exit
    else:
        pass


get_questions_geog(), get_questions_science(), get_questions_politics()
