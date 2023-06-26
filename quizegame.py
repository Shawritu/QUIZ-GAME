questions = ("Name any letter not to apppear  in the periodic table?: ",
                       "What does USB stands for?: ",
                       "How many brains and how many hearts does an octopus have?: ",
                       "Which statement is correct to see if a is equal to b in python",
                       "When will the while loop continue?: ",
                       "BC Roy awards are given in the field of?:")

options = (("A. V", "B. W", "C. J", "D. D"),
                   ("A. Universal Service Battery ", "B. Unique Service Brand", "C. Universal Service Bus", "D. Universal Serial Bus"),
                   ("A. 7 brains and 2 heart", "B. 9 brains and 2 heart", "C. 8 brains and 3 hearts", "D. 9 brains and 3 hearts"),
                   ("A. if a==b:" , "B. if a=b" , "C. if a!=b" ,"D.if a==b "),
                   ("A. When something is equal to something", "B. when something is greater than something", "C.when something is true", "D. All of these"),
                   ("A. Music", "B. Medicines", "C. Journalism", "D. Environment"))

answers = ("C", "D","D", "A", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
