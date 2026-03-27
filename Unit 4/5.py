import matplotlib.pyplot as plt

companies = []
employees = []

for i in range(5):
    name = input(f"Enter name of company {i+1}: ")
    size = int(input(f"Enter number of employees in {name}: "))
    
    companies.append(name)
    employees.append(size)

plt.bar(companies, employees)

plt.xlabel("Companies")
plt.ylabel("Number of Employees")
plt.title("Employee Size of Companies")

plt.show()
