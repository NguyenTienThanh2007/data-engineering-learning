vaccination_records = [
    {"country": "Vietnam", "year": 2024, "coverage": 88.0},
    {"country": "Australia", "year": 2025, "coverage": 85.0},
    {"country": "Vietnam", "year": 2025, "coverage": 95.0},
    {"country": "Japan", "year": 2025, "coverage": 90.0}
]
matching_records = []
search_country = input("Enter country: ")
for i in vaccination_records:
    if i['country'].lower() == search_country.lower():
        matching_records.append(i)
if len(matching_records) > 0 :
    for j in matching_records:
        print(f'{j['country']} - {j['year']}: {j['coverage']}')
    print(f'Matching records: {len(matching_records)}')
else:
    print('No matching records')
    
    