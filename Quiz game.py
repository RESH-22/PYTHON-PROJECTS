questions = {
    "What is the capital of India?": "Delhi",
    "Who developed Python?": "Guido van Rossum",
    "What is 5 + 7?": "12"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", answer)

print("Your score:", score)
