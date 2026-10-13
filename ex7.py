import xlsxwriter
workbook = xlsxwriter.Workbook('sales_chart.xlsx')
worksheet = workbook.add_worksheet()
data = [
    ['Month', 'Sales', 'Profit'],
    ['Jan', 5000, 1200],
    ['Feb', 7000, 1500],
    ['Mar', 6000, 1300],
    ['Apr', 8000, 1700],
    ['May', 7500, 1600],
]
for row_num, row_data in enumerate(data):
    worksheet.write_row(row_num, 0, row_data)
chart = workbook.add_chart({'type': 'column'})
chart.add_series({
    'name':       '=Sheet1!$B$1',               # Sales header
    'categories': '=Sheet1!$A$2:$A$6',          # Months
    'values':     '=Sheet1!$B$2:$B$6',          # Sales data
    'fill':       {'color': '#5ABA10'},
})
chart.add_series({
    'name':       '=Sheet1!$C$1',               # Profit header
    'categories': '=Sheet1!$A$2:$A$6',          # Months
    'values':     '=Sheet1!$C$2:$C$6',          # Profit data
    'fill':       {'color': '#FE110E'},
})
chart.set_title({'name': 'Monthly Sales and Profit'})
chart.set_x_axis({'name': 'Month'})
chart.set_y_axis({'name': 'Amount', 'major_gridlines': {'visible': False}})
worksheet.insert_chart('E2', chart)
workbook.close()
print("Excel file 'sales_chart.xlsx' created with chart.")
