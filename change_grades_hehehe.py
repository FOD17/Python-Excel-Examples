import pandas as pd

# Read the CSV file
df = pd.read_csv('Classroom.csv')

# Alter the grades
df.loc[df['First Name'] == 'Bernie', 'Grade'] = 'A'
df.loc[df['First Name'] == 'Sarah', 'Grade'] = 'C'

# Save the updated data to a new CSV file
df.to_csv('Classroom_updated.csv', index=False)

# Display the updated dataframe
print("Updated Dataframe:")
print(df)
