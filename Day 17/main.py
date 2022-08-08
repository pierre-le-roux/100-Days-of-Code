from question import Question
from quiz_brain import QuizBrain
from alive_progress import alive_bar


def main():

    question_bank = []

    n_questions = int(input('How many questions would you like to answer? '))
    print('Generating your questions: ')

    with alive_bar(n_questions) as bar:
        for i in range(n_questions):
            question_bank.append(Question())
            bar()

    print('\n')
    quiz = QuizBrain(question_bank)

    while not quiz.end_of_quiz():
        quiz.is_correct()


if __name__ == '__main__':
    main()
