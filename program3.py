# Program #3: Average Rainfall
#Author: Zepora
#Date: 9/26/2025
#Title: Average Rainfall Calculator

# Program #3: Average Rainfall
years = int(input("Enter number of years: "))

total_rainfall = 0
total_months = years * 12

for year in range(1, years + 1):
    print(f"Year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"  Enter rainfall (in inches) for month {month}: "))
        total_rainfall += rainfall

average_rainfall = total_rainfall / total_months

print("\nResults:")
print("Total months:", total_months)
print("Total rainfall:", total_rainfall, "inches")
print("Average rainfall per month:", average_rainfall, "inches")
