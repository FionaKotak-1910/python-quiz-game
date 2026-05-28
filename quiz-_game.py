# quiz_game.py
# Tech Quiz Game — FY Computer IT Level
# Topics: Programming basics, networking, OS, web, data types
# Created by: Fiona Kotak | KJSCE

import random
import time

# ══════════════════════════════════════════
# QUESTION BANK — FY IT Level
# ══════════════════════════════════════════

questions = [

    # ── PYTHON ──
    {
        "question": "What is the output of: print(type(10))?",
        "options": ["A) <class 'int'>", "B) <class 'str'>", "C) <class 'float'>", "D) <class 'num'>"],
        "answer": "A",
        "topic": "Python"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) fun", "C) def", "D) define"],
        "answer": "C",
        "topic": "Python"
    },
    {
        "question": "What does len('hello') return?",
        "options": ["A) 4", "B) 6", "C) 5", "D) Error"],
        "answer": "C",
        "topic": "Python"
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "options": ["A) tuple", "B) string", "C) int", "D) list"],
        "answer": "D",
        "topic": "Python"
    },
    {
        "question": "What symbol is used for single-line comments in Python?",
        "options": ["A) //", "B) #", "C) /*", "D) --"],
        "answer": "B",
        "topic": "Python"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["A) 6", "B) 9", "C) 8", "D) 5"],
        "answer": "C",
        "topic": "Python"
    },

    # ── JAVA ──
    {
        "question": "Which concept in OOP restricts direct access to an object's data?",
        "options": ["A) Inheritance", "B) Polymorphism", "C) Encapsulation", "D) Abstraction"],
        "answer": "C",
        "topic": "Java / OOP"
    },
    {
        "question": "What is the default value of an int variable in Java?",
        "options": ["A) null", "B) 1", "C) undefined", "D) 0"],
        "answer": "D",
        "topic": "Java / OOP"
    },
    {
        "question": "Which method is the entry point of a Java program?",
        "options": ["A) start()", "B) run()", "C) main()", "D) init()"],
        "answer": "C",
        "topic": "Java / OOP"
    },
    {
        "question": "What does 'new' keyword do in Java?",
        "options": ["A) Declares a variable", "B) Creates an object in memory", "C) Imports a class", "D) Ends a loop"],
        "answer": "B",
        "topic": "Java / OOP"
    },
    {
        "question": "Which OOP principle allows a child class to use methods of a parent class?",
        "options": ["A) Encapsulation", "B) Abstraction", "C) Inheritance", "D) Overloading"],
        "answer": "C",
        "topic": "Java / OOP"
    },

    # ── C PROGRAMMING ──
    {
        "question": "Which header file is needed for printf() in C?",
        "options": ["A) stdlib.h", "B) math.h", "C) string.h", "D) stdio.h"],
        "answer": "D",
        "topic": "C Programming"
    },
    {
        "question": "What is the size of an int in C (on a 32-bit system)?",
        "options": ["A) 1 byte", "B) 8 bytes", "C) 4 bytes", "D) 2 bytes"],
        "answer": "C",
        "topic": "C Programming"
    },
    {
        "question": "Which loop is guaranteed to execute at least once in C?",
        "options": ["A) for loop", "B) while loop", "C) do-while loop", "D) None of the above"],
        "answer": "C",
        "topic": "C Programming"
    },
    {
        "question": "What does '%d' represent in a printf statement?",
        "options": ["A) Float", "B) Character", "C) String", "D) Integer"],
        "answer": "D",
        "topic": "C Programming"
    },

    # ── HTML / CSS ──
    {
        "question": "Which HTML tag is used to link an external CSS file?",
        "options": ["A) <style>", "B) <css>", "C) <link>", "D) <script>"],
        "answer": "C",
        "topic": "HTML / CSS"
    },
    {
        "question": "What does CSS stand for?",
        "options": ["A) Computer Style Sheets", "B) Cascading Style Sheets", "C) Creative Style System", "D) Colorful Style Syntax"],
        "answer": "B",
        "topic": "HTML / CSS"
    },
    {
        "question": "Which property in CSS is used to change text colour?",
        "options": ["A) font-color", "B) text-color", "C) color", "D) foreground"],
        "answer": "C",
        "topic": "HTML / CSS"
    },
    {
        "question": "What does the <a> tag do in HTML?",
        "options": ["A) Creates an image", "B) Creates a hyperlink", "C) Creates a button", "D) Adds an alert"],
        "answer": "B",
        "topic": "HTML / CSS"
    },

    # ── NETWORKING & OS ──
    {
        "question": "What does IP stand for?",
        "options": ["A) Internet Processor", "B) Internal Protocol", "C) Internet Protocol", "D) Integrated Package"],
        "answer": "C",
        "topic": "Networking"
    },
    {
        "question": "Which layer of the OSI model is responsible for routing?",
        "options": ["A) Data Link", "B) Transport", "C) Physical", "D) Network"],
        "answer": "D",
        "topic": "Networking"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A) Read Access Memory", "B) Random Access Memory", "C) Rapid Application Memory", "D) Runtime Active Module"],
        "answer": "B",
        "topic": "Computer Basics"
    },
    {
        "question": "Which of these is NOT an operating system?",
        "options": ["A) Ubuntu", "B) macOS", "C) Python", "D) Windows"],
        "answer": "C",
        "topic": "Computer Basics"
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["A) HyperText Transfer Protocol", "B) High Tech Transfer Process", "C) HyperText Transmission Port", "D) Home Tool Transfer Protocol"],
        "answer": "A",
        "topic": "Networking"
    },
    {
        "question": "Which data structure works on LIFO principle?",
        "options": ["A) Queue", "B) Array", "C) Stack", "D) Linked List"],
        "answer": "C",
        "topic": "Data Structures"
    },
    {
        "question": "What is the binary representation of the decimal number 5?",
        "options": ["A) 110", "B) 011", "C) 100", "D) 101"],
        "answer": "D",
        "topic": "Computer Basics"
    },
    {
        "question": "Which of these is a compiled language?",
        "options": ["A) Python", "B) JavaScript", "C) Java", "D) HTML"],
        "answer": "C",
        "topic": "Programming Concepts"
    },
]


# ══════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════

def display_banner():
    print("=" * 55)
    print("     FY IT TECH QUIZ — KJSCE Edition")
    print("   Topics: Python | Java | C | HTML/CSS | Networking")
    print("=" * 55)

def display_score(score, total, topic_scores):
    print("\n" + "=" * 55)
    print("                QUIZ RESULTS")
    print("=" * 55)
    print(f"  Final Score  : {score} / {total}")
    percentage = (score / total) * 100
    print(f"  Percentage   : {percentage:.1f}%")

    # Grade
    if percentage >= 90:
        grade = "S — Outstanding! "
    elif percentage >= 75:
        grade = "A — Excellent! "
    elif percentage >= 60:
        grade = "B — Good job! "
    elif percentage >= 45:
        grade = "C — Keep going! "
    else:
        grade = "D — Needs revision! "

    print(f"  Grade        : {grade}")
    print("\n   Score by Topic:")
    print("  " + "-" * 40)
    for topic, data in topic_scores.items():
        t_score = data['correct']
        t_total = data['total']
        bar = "" * t_score + "░" * (t_total - t_score)
        print(f"  {topic:<22} {bar}  {t_score}/{t_total}")
    print("=" * 55)

def get_difficulty():
    print("\nSelect difficulty:")
    print("  1. Easy   — 10 questions")
    print("  2. Medium — 15 questions")
    print("  3. Hard   — All 25 questions")
    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return 10
        elif choice == "2":
            return 15
        elif choice == "3":
            return len(questions)
        else:
            print("Invalid! Enter 1, 2, or 3.")


# ══════════════════════════════════════════
# MAIN GAME FUNCTION
# ══════════════════════════════════════════

def run_quiz():
    display_banner()

    # Get player name
    name = input("\nEnter your name: ").strip()
    if not name:
        name = "Player"

    print(f"\nWelcome, {name}! Let's test your FY IT knowledge ")
    time.sleep(1)

    # Get difficulty
    num_questions = get_difficulty()

    # Shuffle and pick questions
    selected = random.sample(questions, num_questions)

    score = 0
    topic_scores = {}
    wrong_questions = []

    print(f"\n  Starting quiz — {num_questions} questions\n")
    time.sleep(1)

    # ── QUESTION LOOP ──
    for i, q in enumerate(selected, 1):
        topic = q["topic"]

        # Track topic scores
        if topic not in topic_scores:
            topic_scores[topic] = {"correct": 0, "total": 0}
        topic_scores[topic]["total"] += 1

        print(f"\n{'─' * 50}")
        print(f"  Q{i} of {num_questions}  |  Topic: {topic}")
        print(f"{'─' * 50}")
        print(f"  {q['question']}\n")
        for option in q["options"]:
            print(f"    {option}")

        # Get answer
        while True:
            answer = input("\n  Your answer (A/B/C/D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("   Please enter A, B, C, or D only.")

        # Check answer
        if answer == q["answer"]:
            print("    Correct!")
            score += 1
            topic_scores[topic]["correct"] += 1
        else:
            print(f"    Wrong! Correct answer was: {q['answer']}")
            wrong_questions.append(q)

        time.sleep(0.5)

    # ── RESULTS ──
    display_score(score, num_questions, topic_scores)

    # Show wrong answers for revision
    if wrong_questions:
        show_wrong = input("\n📖 Want to review questions you got wrong? (yes/no): ").strip().lower()
        if show_wrong == "yes":
            print("\n" + "=" * 55)
            print("           REVISION — Questions You Missed")
            print("=" * 55)
            for i, q in enumerate(wrong_questions, 1):
                print(f"\n  {i}. {q['question']}")
                for option in q["options"]:
                    print(f"     {option}")
                print(f"   Correct Answer: {q['answer']}")

    # Play again?
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again == "yes":
        print("\n")
        run_quiz()
    else:
        print(f"\nThanks for playing, {name}! Keep learning ")
        


# ══════════════════════════════════════════
# RUN
# ══════════════════════════════════════════

if __name__ == "__main__":
    run_quiz()
