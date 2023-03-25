

class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_question(self, answer):
        return self.question_number < len(self.question_list)

    def next_queston(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q{self.question_number}: {current_question.text}. (True or Flase)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, conrect_ans):
        if user_ans.lower() == conrect_ans.lower():
            print("You got it right")
            self.score += 1
        else:
            print("ur are wrong")
        print(f"the conrect ans is {conrect_ans}")
        print(f"ur current score is: {self.score}/{self.question_number}")
