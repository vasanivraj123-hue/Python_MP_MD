import matplotlib.pyplot as plt

profits = []
years = []

print("Enter profit for 5 years:")

for i in range(5):
    year = input(f"Enter Year {i+1}: ")
    profit = float(input(f"Enter Profit for {year}: "))
    
    years.append(year)
    profits.append(profit)

plt.plot(years, profits, marker='o')

plt.xlabel("Years")
plt.ylabel("Profit")
plt.title("Profit of 5 Years")

plt.grid()

plt.show()
