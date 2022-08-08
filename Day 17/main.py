from question import Question
from quiz_brain import QuizBrain
import requests


def main():

    question_bank = []

    n_questions = int(input('How many questions would you like to answer? '))
    print('Generating your questions: ')
    r = requests.get("https://opentdb.com/api.php?" +
                     f"amount={n_questions}&type=boolean")
    questions = r.json()['results']

    for question in questions:
        text = question['question']\
            .replace('&quot;', '\'')\
            .replace('&#039;', '\'')
        answer = question['correct_answer'].lower()
        question_bank.append(Question(text, answer))

    print('\n')
    quiz = QuizBrain(question_bank)

    while not quiz.end_of_quiz():
        quiz.is_correct()


if __name__ == '__main__':
    main()
