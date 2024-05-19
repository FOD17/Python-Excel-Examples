import pandas as pd

# Create a sample dataframe
data = {
    'First Name': ['Lauren'],
    'Last Name': ['Asthma'],
    'Grade': ['C']
}
df = pd.DataFrame(data)

# Check if the file exists
try:
    # Read the existing CSV file
    existing_df = pd.read_csv('Classroom.csv')

    # Append the new data
    df = pd.concat([existing_df, df])

except FileNotFoundError:
    # If the file does not exist, the dataframe is already prepared
    pass

# Write the dataframe to the CSV file
df.to_csv('Classroom.csv', index=False)

# Read an Excel file
df = pd.read_csv('Classroom.csv')

# Display entire csv file
print(df)
