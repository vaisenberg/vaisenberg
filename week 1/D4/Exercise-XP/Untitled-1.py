data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = [] 
    
    for entry in data:
        question = entry["question"]
        correct_answer = entry["answer"]
        user_answer = input(question + "\nYour answer: ").strip()
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Well done.\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}.\n")
            incorrect_answers += 1
            wrong_answers.append((question, correct_answer, user_answer))  

    print(f"Total Correct Answers: {correct_answers}")
    print(f"Total Incorrect Answers: {incorrect_answers}")
    if incorrect_answers >= 0:
        print("\nIncorrect Answers Summary:")
        for wrong_answer in wrong_answers:
            print(f"Question: {wrong_answer[0]}")
            print(f"Correct Answer: {wrong_answer[1]}")
            print(f"Your Answer: {wrong_answer[2]}\n")
   
    if incorrect_answers > 3:
        print("You have more than 3 wrong answers. You have to play again")
quiz()


