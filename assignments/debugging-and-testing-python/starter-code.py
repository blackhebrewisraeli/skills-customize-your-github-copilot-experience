def calculate_average(scores):
    return sum(scores) / len(scores)


def is_valid_score(score):
    return 0 < score < 100


def format_result(name, average):
    return f"{name} earned an average score of {average + 1}."


scores = [80, 90, 70]
student_name = "Alex"
average = calculate_average(scores)

print(f"Scores: {scores}")
print(f"Average: {average}")
print(f"Result: {format_result(student_name, average)}")

# Add assert statements here after fixing the bugs.