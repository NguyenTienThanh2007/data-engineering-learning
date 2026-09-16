'''Đọc file vaccination_data.csv:

country,year,coverage
Vietnam,2024,88.0
Australia,2025,85.0
Vietnam,2025,95.0
Japan,2025,90.0
Thailand,2025,65.0

Phân loại status:

coverage >= 90: "High"
coverage >= 70: "Medium"
Còn lại: "Low"

Sau đó lưu vào file mới vaccination_with_status.csv.

Kết quả mong muốn:

country,year,coverage,status
Vietnam,2024,88.0,Medium
Australia,2025,85.0,Medium
Vietnam,2025,95.0,High
Japan,2025,90.0,High
Thailand,2025,65.0,Low'''
import csv
matching_records = []
with open ("vaccination_data.csv", "r", newline = "") as input_file :
    reader = csv.DictReader(input_file)
    for i in reader :
        country = i["country"]
        year = int(i['year'])
        coverage = float(i['coverage'])
        if coverage >=90 :
            status = "High"
        elif coverage >= 70:
            status = "Medium"
        else:
            status = "Low"
        record = {
            "country" : country,
            "year" : year,
            "coverage" : coverage,
            "status" : status
        }
        matching_records.append(record)

with open ("vaccination_with_status.csv", "w", newline = "") as output_file:
    fieldnames = ["country", "year", "coverage", "status"]
    writer = csv.DictWriter(output_file, fieldnames = fieldnames)
    writer.writeheader()
    for z in matching_records:
        writer.writerow(z)
print(f'Saved records: {len(matching_records)}')

            
            
    
                   
    