import pandas as pd
import matplotlib.pyplot as plt

# matplotlib
# pip3 install matplotlib

# Read the CSV file
df = pd.read_csv('Classroom.csv')

# Plot the grade distribution
grade_counts = df['Grade'].value_counts()
grade_counts.plot(kind='bar', color='skyblue')
plt.title('Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.show()
