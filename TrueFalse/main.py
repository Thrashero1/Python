from question_model import Question
from QuestionData import question_data
numb = 0
question_bank = []
for question in question_data:
     question_bank.append(Question(question['text'], question['answer']))
