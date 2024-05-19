import pandas as pd

# Read the CSV file
df = pd.read_csv('Classroom.csv')

# Add a new column for pass/fail
df['Pass/Fail'] = df['Grade'].apply(lambda x: 'Pass' if x in ['A', 'B', 'C'] else 'Fail')

# Save the updated dataframe to a new CSV file
df.to_csv('Classroom_PassFail.csv', index=False)

# Display the updated dataframe
print("Updated Dataframe with Pass/Fail:")
print(df)
