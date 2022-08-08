class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank

    def ask_question(self):
        question = self.question_bank[self.question_number].text
        self.question_number += 1

        choice = input(f'Q.{self.question_number}: ' +
                       f'{question} [true/false]: ').lower()
        return choice

    def is_correct(self):
        answer = self.question_bank[self.question_number].answer

        if self.ask_question() == answer:
            self.score += 1
            print('Correct answer,',
                  f'current score {self.score}/{self.question_number}\n\n')
            return True
        else:
            print('Incorrect answer,',
                  f'current score {self.score}/{self.question_number}\n\n')
            return False

    def end_of_quiz(self):
        if self.question_number == len(self.question_bank):
            print("You've answered all the qeustions,",
                  f'your final score is {self.score}/{self.question_number}')
            return True
        else:
            return False
