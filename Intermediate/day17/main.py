from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # question1 =
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

end_game = False
while quiz_brain.still_has_question:
    quiz_brain.next_queston()
       



