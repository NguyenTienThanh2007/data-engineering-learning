vaccination_records = [
    {"country": "Vietnam", "coverage": 95.0},
    {"country": "Australia", "coverage": 85.0},
    {"country": "Japan", "coverage": 90.0},
    {"country": "Thailand", "coverage": 70.0}
]
high_coverage_records =[]
for i in vaccination_records:
    if i['coverage'] >= 90:
        high_coverage_records.append(i)

if len(high_coverage_records) > 0:
    for j in high_coverage_records:
        
        print(f'{j['country']}: {j['coverage']}')
    print(f'Matching records: {len(high_coverage_records)}')
else:
    print("No matching records")
