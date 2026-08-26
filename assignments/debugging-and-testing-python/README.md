# 📘 Assignment: Debugging and Testing Python Programs

## 🎯 Objective

Practice reading Python error messages, finding bugs, and using simple tests to check whether a program works correctly. You will repair a small grade calculator and add tests that make future mistakes easier to find.

## 📝 Tasks

### 🛠️ Fix the Grade Calculator

#### Description

Open the provided starter code and run the program. It contains three bugs in the grade calculator. Use the error messages, printed output, and careful code reading to find and fix each problem.

#### Requirements

Completed program should:

- Run without Python errors
- Correctly calculate the average of a list of scores
- Accept scores from 0 through 100 as valid scores
- Format a student's name and average in the expected result message
- Explain in a short comment or note what each bug was and how you fixed it

Example:

```text
Scores: [80, 90, 70]
Average: 80.0
Result: Alex earned an average score of 80.0.
```

### 🛠️ Add Tests and Handle an Edge Case

#### Description

Write `assert` statements that check each function in the grade calculator. Then update the program so that trying to calculate an average with no scores returns `0` instead of causing an error.

#### Requirements

Completed program should:

- Include at least two tests for `calculate_average()`
- Include tests for both valid and invalid scores in `is_valid_score()`
- Include a test for `format_result()`
- Include a test confirming that an empty score list returns an average of `0`
- Keep all tests passing after the bugs are fixed

Example:

```python
assert calculate_average([80, 90, 70]) == 80
assert calculate_average([]) == 0
assert is_valid_score(100) is True
assert is_valid_score(101) is False
```