from question import Question
from question_banks import question_banks
from question_utils import Utils
from quiz_brains import QuizBrain
questions = []
questions = Utils.map_array_of_dict_into_array_of_object(question_banks, questions)

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")