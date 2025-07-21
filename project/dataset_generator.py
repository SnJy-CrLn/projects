import pandas as pd
import random

first_names = ['John', 'David', 'Michael', 'James', 'Robert', 'William', 'Mary', 'Patricia',
              'Linda', 'Barbara', 'Elizabeth', 'Susan', 'Jennifer', 'Jessica', 'Amanda']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia',
              'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Harris']

def generate_random_name():
  return random.choice(first_names) + ' ' + random.choice(last_names)


def generate_random_marks():
  return random.randint(0, 100)

# Generate data
data = {'Student Name': [generate_random_name() for _ in range(150)]}
for i in range(1, 11):
  data[f'Exam{i}'] = [generate_random_marks() for _ in range(150)]

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv('student_marks_150.csv', index=False)