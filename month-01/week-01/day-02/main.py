
'''coverage > 100   → Review required
coverage >= 90   → Excellent coverage
coverage >= 80   → Good coverage
coverage >= 50   → Needs improvement
coverage < 50    → Critical coverage'''

country = input("Enter your country")
year = int(input("Enter year: "))
target_population = int(input("Enter target population: "))
doses_given = int(input("Enter doses given: "))
if target_population <= 0:
    print("Target population must be greater than zero.")
elif doses_given < 0:
    print("Doses given cannot be negative.")
else:
    coverage = round((doses_given / target_population) * 100, 2)
    
    if coverage >100:
        status = "Review required"
    elif coverage >= 90:
        status = "Excellent coverage"
    elif coverage >= 80:
        status = "Good coverage"
    elif coverage >= 50:
        status = "Needs improvement"
    else:
        status = "Critical coverage"
        
print('\n Report')
print(f'coverage: {coverage}%')
print(f'Status: {status}')
