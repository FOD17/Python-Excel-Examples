import pandas as pd

df = pd.read_csv('Classroom.csv')

# Filter the dataframe to only include students with grades A or B
filtered_by_grade_good_students = df[df['Grade'].isin(['A', 'B'])]

# Filter the dataframe to only include students with grades C or below
filtered_by_grade_failing_life = df[df['Grade'].isin(['C', 'D', 'F'])]


# Display the filtered dataframe
print("Filtered by Grade, A and B:")
print(filtered_by_grade_good_students)

# Displat the filtered dataframe
print("Filtered by Grade, C and below:")
print(filtered_by_grade_failing_life)

# Filter the dataframe to only include students with specific first names
filtered_by_name = df[df['First Name'].isin(['Bob', 'Sarah'])]

# Display the filtered dataframe
print("Filtered by Name:")
print(filtered_by_name)
