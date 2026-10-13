import pandas as pd
data = {
    'EmployeeName': ['John', 'Alice', 'Bob', 'Emma'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [50000, 60000, 55000, 52000]
}
df = pd.DataFrame(data)
salaries = df['Salary']        
hr_employees = df[df['Department'] == 'HR']  
total_salary = salaries.sum()
average_salary = salaries.mean()
df['Bonus'] = df['Salary'] * 0.1
high_salary = df[df['Salary'] > 55000]
total_salary = salaries.sum()
average_salary = salaries.mean()
print(df)
