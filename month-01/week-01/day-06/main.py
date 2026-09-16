def cal_coverage (target_population, doses_given) :
    coverage  = round((doses_given / target_population *100), 2)
    return coverage
vaccination_records = []
num_record = int(input("Enter number of records: "))
for i in range(1, num_record + 1 ):
    print(f'===Records {i}===')
    country = input("Enter country: ")
    year = int(input("Enter year: "))
    target_population = int(input("Enter population: "))
    doses_given = int(input("Enter doses given "))
    if target_population <= 0 :
        print("Invalid")
        continue
    if doses_given <0 :
        print('Invalid')
        continue
    coverage = cal_coverage (target_population, doses_given) 
    
    records ={
        "country" : country,
        "year" : year,
        "target_population": target_population,
        "doses_given" : doses_given,
        "coverage" : coverage
    }
    vaccination_records.append(records)
if len(vaccination_records) > 0 :
    total_coverage = 0
    highest_records = vaccination_records[0]
    print(f'===Vaccination Record===')
    for j in vaccination_records:
        print(f'Country: {j['country']}')
        print(f'Year: {j['year']}')
        print(f'Population: {j['target_population']}')
        print(f'Doses given: {j['doses_given']}')
        print(f'Coverage: {j['coverage']}')
        total_coverage += j['coverage']
        if highest_records['coverage'] < j['coverage']:
            highest_records = j
    avg_coverage = round(total_coverage/ len(vaccination_records), 2)
    print('===Summary===')
    print(f'Valid records: {len(vaccination_records)}')
    print(f'Average coverage: {avg_coverage}%')
    print(f'Highest coverage: {highest_records['coverage']}')
    print(f'Country with highest coverage: {highest_records['country']}')
else:
    print('Invalid')
            
        
    
    
    
        
    
        
    
    

    
    
    

    
    


