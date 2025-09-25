





# -------------------------------
# Stack Practical Tasks (Rwanda)
# -------------------------------

# Task 1: In MoMo, push ["Step1", "Step2", "Step3"]. Undo last.
print("Task 1: MoMo Transaction Steps")
stack_momo = []  # empty stack

# Push operations
stack_momo.append("Step1")
stack_momo.append("Step2")
stack_momo.append("Step3")
print("After pushing:", stack_momo)

# Undo last (pop)
stack_momo.pop()
print("After undo (pop):", stack_momo)
print("Remaining steps:", stack_momo)
print("-" * 40)

# Task 2: UR pushes ["Quiz1", "Quiz2", "Quiz3"]. Pop all.
print("Task 2: UR Quizzes")
stack_quiz = []  # empty stack

# Push operations
stack_quiz.append("Quiz1")
stack_quiz.append("Quiz2")
stack_quiz.append("Quiz3")
print("After pushing:", stack_quiz)

# Pop all
stack_quiz.pop()
stack_quiz.pop()
stack_quiz.pop()
print("After popping all:", stack_quiz)
print("Remaining quizzes:", stack_quiz)
