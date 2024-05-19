import pandas as pd

# Read the CSV file
df = pd.read_csv('Classroom.csv')

# Count the number of students per grade
grade_counts = df['Grade'].value_counts()
print("Number of Students per Grade:")
print(grade_counts)

# Read the updated CSV file
df = pd.read_csv('Classroom_updated.csv')

# Count the number of students per grade
grade_counts = df['Grade'].value_counts()
print("Number of Students per Grade:")
print(grade_counts)
