from openpyxl import Workbook

# Create a new workbook
wb = Workbook()
sheet = wb.active

# Add data
sheet.title = "EmployeeData"
sheet.append(["ID", "Name", "Department"])  # Adding header
sheet.append([1, "John Doe", "HR"])
sheet.append([2, "Jane Smith", "IT"])
sheet.append([3, "Sam Wilson", "Finance"])

# Save the workbook
wb.save("employee_data.xlsx")
print("Data added successfully!")
