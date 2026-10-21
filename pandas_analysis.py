import pandas as pd

# Read employee data
df = pd.read_csv("employees.csv")

print("Employee Data")
print(df)

# Total Employees
print("\nTotal Employees:")
print(len(df))

# Average Salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# Highest Salary Employee
print("\nHighest Salary Employee:")
print(df.loc[df["Salary"].idxmax()])

# Lowest Salary Employee
print("\nLowest Salary Employee:")
print(df.loc[df["Salary"].idxmin()])

# Highest Performance Employee
print("\nHighest Performance Employee:")
print(df.loc[df["Performance score"].idxmax()])

# Employees Below Attendance 75
print("\nEmployees Below Attendance 75:")
print(df[df["Attendance"] < 75])

# Employees Above Salary 50000
print("\nEmployees Above Salary 50000:")
print(df[df["Salary"] > 50000])

# High Performance Employees (>85)
print("\nHigh Performance Employees:")
print(df[df["Performance score"] > 85])

# Employees Department Wise
print("\nEmployees Department Wise:")
print(df.groupby("Department").size())

# Average Salary Department Wise
print("\nAverage Salary Department Wise:")
print(df.groupby("Department")["Salary"].mean())

# Employee Count Department Wise
print("\nEmployee Count Department Wise:")
print(df.groupby("Department").size())

# Maximum Salary Department Wise
print("\nMaximum Salary Department Wise:")
print(df.groupby("Department")["Salary"].max())

# Minimum Salary Department Wise
print("\nMinimum Salary Department Wise:")
print(df.groupby("Department")["Salary"].min())

# Average Attendance
print("\nAverage Attendance:")
print(df["Attendance"].mean())

# Average Performance Score
print("\nAverage Performance Score:")
print(df["Performance score"].mean())

# Top 5 Highest Salary Employees
print("\nTop 5 Highest Salary Employees:")
print(df.nlargest(5, "Salary"))

# Top 5 Lowest Salary Employees
print("\nTop 5 Lowest Salary Employees:")
print(df.nsmallest(5, "Salary"))

# Salary Ascending
print("\nSalary Ascending:")
print(df.sort_values(by="Salary"))

# Salary Descending
print("\nSalary Descending:")
print(df.sort_values(by="Salary", ascending=False))