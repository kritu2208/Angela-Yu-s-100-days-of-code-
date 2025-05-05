from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    text = question["text"] 
    answer = question["answer"]
    new_ques = Question(text,answer ) 
    question_bank.append(new_ques)

# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions ():
    quiz.next_question()

print("the quiz ends.")    
print(f"your total score is {quiz.score}/{quiz.question_number}")