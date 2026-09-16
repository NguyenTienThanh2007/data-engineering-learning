country = input("Enter country: ")
year = int(input("Enter year: "))
target_population = int(input("Enter target population: "))
doses_given = int(input("Enter doses given: "))

coverage = doses_given / target_population * 100
coverage = round(coverage, 2)

if coverage > 100:
    status = "Review required: coverage is above 100%"
elif coverage >= 90:
    status = "Excellent coverage"
elif coverage >= 80:
    status = "Good coverage"
elif coverage >= 50:
    status = "Needs improvement"
else:
    status = "Critical coverage"

print("\n--- Vaccination Report ---")
print(f"Country: {country}")
print(f"Year: {year}")
print(f"Coverage: {coverage}%")
print(f"Status: {status}")