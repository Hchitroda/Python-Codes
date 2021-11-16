from questions import questions

questions_prompts = [
    "what color are bananas? \n(a) Red\n(b) yellow\n\n",
    "what color are apple?\n(a) Red\n(b) yellow\n\n",
    "what color are strawberries?\n(a) orange\n(b) black\n\n",
]

questions = [
    questions(questions_prompts[0], "a"),
    questions(questions_prompts[1], "b"),
    questions(questions_prompts[2], "b"),
]

def run_test(questions):
    score = 0 
    for questions in questions:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score += 1 
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)