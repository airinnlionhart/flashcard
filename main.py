import random


# This is a sample Python script.
class Flashcard:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


def play_flashcard_game(list_of_cards):
    score = 0
    total_questions = len(list_of_cards)

    for i, flashcard in enumerate(list_of_cards, 1):
        flashcard.display_question()
        user_answer = int(input("Your answer (enter the option number): "))

        if flashcard.check_answer(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is option", flashcard.correct_option, "\n")

    print("Game Over! Your final score:", score, "/", total_questions)
