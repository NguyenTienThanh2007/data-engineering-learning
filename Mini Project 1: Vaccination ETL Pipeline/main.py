import csv 
import json
def extract_data(filename):
    with open (filename, "r", newline="") as input_file :
        reader = csv.reader(input_file)
        next(reader)
        records = list(reader)
    return records
def transform_data (records) :
    invalid_records = 0 
    clean_records = []
    for i in records:
        country = i[0].strip()
        try : 
            year = int(i[1])
            target_population = int(i[2])
            doses_given = int (i[3])
        except ValueError :
            print (f"Skipped error row {i}")
            invalid_records += 1 
            continue
        if country == "":
            print (f"Skipped error row {i}")
            invalid_records +=1
            continue
        if target_population <= 0 :
            print (f"Skipped error row: {i}")
            invalid_records+= 1 
            continue
        if doses_given <0 :
            print (f"Skipped error row: {i}")
            invalid_records += 1 
            continue
        
        coverage = round ((doses_given/target_population * 100), 2)
        if coverage >= 90:
            status = "High"
        elif coverage >= 70 :
            status = "Medium"
        else:
            status = "Low"
        record = {
            "country": country,
            "year": year,
            "target_population": target_population,
            "doses_given": doses_given,
            "coverage": coverage,
            "status": status
        
        
        }
        clean_records.append (record)
    return clean_records, invalid_records
def load_data (records, filename):
    with open (filename, "w", encoding="utf-8") as output_file :
        json.dump(records, output_file, indent=4, ensure_ascii=False)
data = extract_data ("raw_vaccination_data.csv")
clean_records, invalid_records = transform_data(data)
load_data(clean_records, "clean_vaccination_data.json")

print ("===ETL Summary===")
print (f"Valid records: {len (clean_records)}")
print (f"Invalid records: {invalid_records}")
print(f"Saved to clean_vaccination_data.json")



            
            
            
        
    