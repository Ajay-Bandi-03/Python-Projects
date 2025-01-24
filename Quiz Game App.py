questions = {"What is 2+2?": "4", "What is the capital of France?": "Paris", "What color is the sky?": "Blue"}
score = 0
print("Welcome to the Quiz Game!")
for q, a in questions.items():
    ans = input(f"{q} ").strip()
    if ans.lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print(f"Your final score is {score}/{len(questions)}")
