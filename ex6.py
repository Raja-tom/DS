import pandas as pd
employees = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'DepartmentID': [101, 102, 101]
})

departments = pd.DataFrame({
    'DepartmentID': [101, 102, 103],
    'DepartmentName': ['HR', 'Finance', 'IT']
})

# VLOOKUP: Merge employees with departments on DepartmentID (left join)
merged_df = pd.merge(employees, departments, on='DepartmentID', how='left')
print("VLOOKUP Equivalent (Merge):")
print(merged_df)
print("\n")

# Sample data for Pivot Table equivalent
sales_data = pd.DataFrame({
    'SalesPerson': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie'],
    'Region': ['North', 'South', 'South', 'North', 'North'],
    'Sales': [1200, 800, 500, 600, 1000]
})

# Pivot table: total sales by SalesPerson and Region
pivot_table = pd.pivot_table(sales_data, values='Sales',
                             index='SalesPerson',
                             columns='Region',
                             aggfunc='sum',
                             fill_value=0)
print("Pivot Table Equivalent:")
print(pivot_table)
