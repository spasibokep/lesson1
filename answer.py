answers = {'привет':'И тебе привет', 'как дела':'Лучше всех', 'пока':'Увидимся'}
def get_answer (question, answers):
    question = str(question).lower()
    #print(question)
    result = answers.get(question, 'Try again')
    return result

user = input('Скажи привет')
a = get_answer(user, answers)
print(a)