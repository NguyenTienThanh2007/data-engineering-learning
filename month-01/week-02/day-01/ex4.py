'''Hãy:

Tạo file vaccination_data.csv.
Ghi dòng tiêu đề:
country,year,coverage
Dùng for ghi từng record vào file.
Sau khi ghi xong, in:
CSV file saved successfully'''


vaccination_records = [
    {"country": "Vietnam", "year": 2024, "coverage": 88.0},
    {"country": "Australia", "year": 2025, "coverage": 85.0},
    {"country": "Vietnam", "year": 2025, "coverage": 95.0},
    {"country": "Japan", "year": 2025, "coverage": 90.0}
]
import csv
with open ("vaccination_data.csv", "w", newline = "") as file :
    writer = csv.writer(file)
    writer.writerow (["country", "year", "coverage"])
    for i in vaccination_records:
        writer.writerow ([
            i['country'],
            i['year'],
            i['coverage']
            
        ])
print("CSV file saved successfully")


        
