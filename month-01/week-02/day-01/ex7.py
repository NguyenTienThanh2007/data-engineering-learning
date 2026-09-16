'''Đọc file vaccination_data.csv, sau đó chỉ in những record có coverage từ 90% trở lên.

Kết quả cần đạt:

Vietnam - 2025: 95.0%
Japan - 2025: 90.0%
Matching records: 2'''
import csv
matching_records = []
with open ("vaccination_data.csv" , "r", newline = "" ) as file :
    reader = csv.DictReader(file)
    for i in reader :
        country = i["country"]
        year = int(i["year"]) 
        coverage = float(i["coverage"])
        if coverage >= 90:
            records = {
                "country" : country,
                "year" : year,
                "coverage": coverage
                
            }
            matching_records.append(records)
if len(matching_records) > 0 :
    print ('Summary')
    for records in matching_records:
        print(f'{records['country']} - {records["year"]} : {records["coverage"]}')
else:
    print("No matching records")
            