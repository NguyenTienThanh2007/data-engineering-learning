'''Đây là một quy trình ETL nhỏ:

Extract: đọc vaccination_data.csv.
Transform: lọc coverage từ 90%.
Load: ghi vào high_coverage.csv.

File đầu vào:

country,year,coverage
Vietnam,2024,88.0
Australia,2025,85.0
Vietnam,2025,95.0
Japan,2025,90.0

File kết quả cần tạo:

country,year,coverage
Vietnam,2025,95.0
Japan,2025,90.0'''
import csv 
high_coverage_records = []
with open ("vaccination_data.csv", "r" , newline = "") as input_file : 
    reader = csv.DictReader(input_file)
    for i in reader : 
        country = i['country']
        year = int(i['year'])
        coverage = float(i['coverage'])
        if coverage >= 90:
            records = {
                "country" : country,
                "year" : year,
                "coverage" : coverage
                
                
            }
            high_coverage_records.append(records)
with open("high_coverage.csv", "w", newline = "") as output_file :
    fieldnames = ["country", "year", "coverage"]
    writer = csv.DictWriter(output_file, fieldnames = fieldnames)
    writer.writeheader()
    for i in high_coverage_records:
        writer.writerow(i)
        
print(f'Saved records: {len(high_coverage_records)}')
    
