from question_model import Question
from QuestionData import question_data
from quizBrain import QuizBrain

question_bank = []
for question in question_data:
     question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)

still_questioning = True

while still_questioning:
     answer = input(quiz.next_question()).capitalize()
     quiz.check_answer(answer)
     still_questioning = quiz.still_has_questions()