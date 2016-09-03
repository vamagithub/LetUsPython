"""
1. Ramesh's basic salary is input  (1. through keyboard 2. through cmd prompt)
2. Dearness Allowance = 40% of basic salary
3. Hour Rent Allowance = 20% of basic salary
4. Calculate Gross Salary - WAP
"""

# cmd prompt Input

from sys import argv

script, basic_salary = argv

# argv input is string
basic_salary = int(basic_salary)  # type casting

# %d - int | %s - string
print("basic salary -cmd prompt:\n%d" % basic_salary)

print("Enter your name as well for our records:\t\n")
name = input(">>")

dearness_allowance = 0.4 * basic_salary
house_rent = 0.2 * basic_salary

print("Welcome %s,to ganpati bank , your gross salary is..\n"%name)
print("\t%d" % (basic_salary + dearness_allowance + house_rent))
