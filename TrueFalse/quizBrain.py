class QuizBrain:
    def __init__(self, quest_list) -> None:
        self.question_number = 0
        self.question_list = quest_list
        self.score = 0
        
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f'Thanks for playing, your final score is: {self.score}/{self.question_number}')
            return False
        
    def next_question(self):
        q_numb = self.question_number
        self.question_number += 1
        question = f'Q{self.question_number}: {self.question_list[q_numb].text} (True/False)? '
        return question
    
    def check_answer(self, answer):
        q_numb = self.question_number
        actual_answer = self.question_list[q_numb - 1].answer
        if answer == actual_answer:
            self.score += 1
            print (f'Correct the answer was {answer} \nyour current score is {self.score}/{q_numb}\n')
        else:
            print (f'Sorry the correct answer was {self.question_list[q_numb].answer} \nyour current score is {self.score}/{q_numb} \n')