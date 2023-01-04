# creare a dict with questions and ans
# variable that tracks the score
# loop through the dict
# display each ques to the user and let them answer
# let them know if the ans is correct or not
# display the final result when complete

quiz = {
    "question1": {
        "question": "What is the capital of Sri Lanka?",
        "answer": "Sri Jayawardane Pura"
    },
    "question2": {
        "question": "What is the capital of Mali?",
        "answer": "Timbuktu"
    },
    "question3": {
        "question": "What is the capital of USA?",
        "answer": "Washington DC"
    },
    "question4": {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    "question5": {
        "question": "What is the capital of Qatar?",
        "answer": "Doha"
    },
    "question6": {
        "question": "What is the capital of Morocco?",
        "answer": "Rabat"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct' + '\n')
        score += 1
        print("Your score is: " + str(score) + '\n')

    else:
        print('Wrong' + '\n')
        print('The Answer is: ' + value["answer"] + '\n')
        print("Your score is: " + str(score) + '\n')

print("Your final score: " + str(score) + "/6")
print("Your Percentage: " + str(int(score/7*100)) + "%") #convert to int before str so that you can concatanate
print("")