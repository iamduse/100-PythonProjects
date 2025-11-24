class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.current_score = 0
        self.question_list = question_list

    def next_question(self, current_q_number):
        current_q_number = self.question_list[self.question_number]
        input(f"{self.question_number, self.question_list} what is this " )


    # check the correct answer method

    # still has a questio
    def still_has_question(self):
        return self.question_number < len(self.question_list)