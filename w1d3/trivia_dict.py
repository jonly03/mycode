#!/usr/bin/env python3
import html
from trivia_data import trivia

question_key = "question"
correct_answer_key = "correct_answer"
incorrect_answers_key = "incorrect_answers"

tries = 3

def get_q_and_a():
    trivia_q = trivia[question_key]
    trivia_correct_answer = html.unescape(trivia[correct_answer_key])
    trivia_incorrect_answers = []

    for incorrect_answer in trivia[incorrect_answers_key]:
        trivia_incorrect_answers.append(html.unescape(incorrect_answer))

    return {"question": trivia_q, "correct_answer": trivia_correct_answer, "incorrect_answers": trivia_incorrect_answers}

def eval_answer(user_input):
    global tries # tells the function to use the global tries variable instead of trying to use a local one (which doesn't exist)

    if user_input.upper() in ['A', 'B', 'C', 'D']:
        tries -= 1
        if user_input.upper() == 'C':
            print(f"Correct answer!sd")
        else:
            if tries > 0:
                try_again(f"Incorrect answer. {tries} more {'tries' if tries > 1 else 'try'}. Try again")
            else:
                print("Out of tries. Correct answer: C")
                return
    else:
        try_again("Invalid option. Enter A, B, C, or D.")

def try_again(msg):
    print(msg, end="\n\n")
    main()

def main():
    global tries # tells the function to use the global tries variable instead of trying to use a local one (which doesn't exist)

    trivia_info = get_q_and_a()

    print(f"{trivia_info[question_key]}")
    print(f"A. {trivia_info[incorrect_answers_key][0]}")
    print(f"B. {trivia_info[incorrect_answers_key][1]}")
    print(f"C. {trivia_info[correct_answer_key]}")
    print(f"D. {trivia_info[incorrect_answers_key][2]}")

    eval_answer(input("Answer (A, B, C, or D): "))

if __name__ == "__main__":
    main()