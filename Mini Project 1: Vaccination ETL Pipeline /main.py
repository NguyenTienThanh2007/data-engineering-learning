import csv
import json
def extract_data (filename) :
    with open (filename, "r", newline = "", encoding= "utf-8") as input_file :
        reader = csv.reader (input_file)
        next (reader)
        records = list(reader)
    return records
def transform_data (records):
    clean_records = []
    invalid_records = 0 
    for i in records :
        country = i[0].strip ()
        try :
            year = int(i[1])
            target_population = int (i[2])
            doses_given = int (i[3])
        except ValueError:
            print (f"Skipped error row : {i}")
            invalid_records +=1
            continue
        if country == "" :
            print(f"Skipped error row: {i}")
            invalid_records += 1
            continue
        if target_population <= 0 :
            print (f"Skipped error row: {i}")
            invalid_records+=1 
            continue
        if doses_given <0:
            print (f"Skipped error row: {i}")
            invalid_records+=1 
            continue 
        coverage = round ((doses_given / target_population * 100 ),2)
        if coverage >= 90 :
            status = "High"
        elif coverage >= 70:
            status = "Medium"
        else:
            status = "Low"
        clean_records_data =  {
            "country": country, 
            "year" : year,
            "target_population": target_population,
            "doses_given": doses_given,
            "coverage": coverage,
            "status": status
        }
        clean_records.append (clean_records_data)
    return clean_records, invalid_records
def calculate_summary (records):
    status_counts ={
        "High" : 0,
        "Medium": 0 ,
        "Low": 0
    }
    total_records = len (records)
    if total_records == 0 :
        return {
            "total_records": 0,
            "average_coverage": 0,
            "highest_coverage": None,
            "highest_country": None,
            "lowest_coverage": None,
            "lowest_country": None,
            "status_counts": status_counts
            
        }
    
    highest_record = records[0]
    lowest_record = records[0]
    total_coverage = 0    
    for record in records:
        total_coverage += record["coverage"]
        status = record["status"]
        status_counts[status] +=1 
        if highest_record["coverage"] <= record["coverage"]:
            highest_record = record
        if lowest_record["coverage"] >= record["coverage"]:
            lowest_record = record
    average_coverage = round ((total_coverage/ total_records),2)
    summary ={
        "total_records": total_records,
        "average_coverage": average_coverage,
        "highest_coverage": highest_record["coverage"],
        "highest_country": highest_record["country"],
        "lowest_coverage": lowest_record["coverage"],
        "lowest_country": lowest_record["country"],
        "status_counts": status_counts
    }
    return summary

def load_data (data, filename):
    with open (filename, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)

records = extract_data("raw_vaccination_data.csv")
clean_records, invalid_records = transform_data(records)
summary = calculate_summary(clean_records)
load_data(clean_records, "clean_vaccination_data.json")
load_data(summary, "vaccination_summary.json")

print (f"\n===ETL Summary===")
print (f"Valid records: {len(clean_records)}")
print (f"Invalid records: {invalid_records}")
print ("\n===Vaccination Summary===")
print (f"Average coverage: {summary['average_coverage']}%")
if summary['total_records'] > 0 :
    print(f"Highest coverage: {summary['highest_country']} - {summary['highest_coverage']}")
    print(f"Lowest coverage: {summary['lowest_country']} - {summary['lowest_coverage']}")
else:
    print("No data records")
print (f"{summary['status_counts']}")
print ("Saved to clean_vaccination_data.json")
print ("Saved to vaccination_summary.json")





    
            
            
            
                                     
        
