import pandas as pd

# Read the CSV file
df = pd.read_csv('Classroom.csv')

# Map grades to numerical values
grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
df['Grade Value'] = df['Grade'].map(grade_mapping)

# Calculate the average grade
average_grade = df['Grade Value'].mean()
print(f"Average Grade: {average_grade:.2f}")

# Optionally map back to letter grades
inverse_grade_mapping = {v: k for k, v in grade_mapping.items()}
print(f"Average Grade (Letter): {inverse_grade_mapping[round(average_grade)]}")
