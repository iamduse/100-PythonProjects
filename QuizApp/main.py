import  data
import question_model
import quiz_brain

# this for loop reads the quiz data and put the values to an object then the object to list of question bank
question_bank = []
for each in data.question_date:
    text = each["text"]
    answer = each["answer"]
    new_question = question_model.QuestionModel(text,answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question(0)



