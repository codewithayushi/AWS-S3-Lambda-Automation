import csv
import random

# File ka naam
filename = "sample_data.csv"

# Header define karna
header = ['id', 'name', 'department', 'salary']

# 100 dummy records banana
departments = ['IT', 'Engineering', 'Cloud', 'HR', 'Finance']
names = ['User_']

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header) # Pehle header likhna
    
    for i in range(1, 101):
        writer.writerow([
            i, 
            f"Employee_{i}", 
            random.choice(departments), 
            random.randint(30000, 90000)
        ])

print(f"Done! {filename} mein 100 records upload (write) ho gaye hain.")