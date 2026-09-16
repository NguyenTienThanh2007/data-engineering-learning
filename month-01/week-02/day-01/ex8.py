'''Hãy ghi dữ liệu vào file vaccination_output.csv bằng csv.DictWriter().

File kết quả phải là:

country,year,coverage
Vietnam,2024,88.0
Australia,2025,85.0
Vietnam,2025,95.0
Japan,2025,90.0'''
vaccination_records = [
    {"country": "Vietnam", "year": 2024, "coverage": 88.0},
    {"country": "Australia", "year": 2025, "coverage": 85.0},
    {"country": "Vietnam", "year": 2025, "coverage": 95.0},
    {"country": "Japan", "year": 2025, "coverage": 90.0}
]
fieldnames = ["country", "year", "coverage"]
import csv 
with open ("vaccination_output", "w", newline = "") as file : 
    writer = csv.DictWriter(file, fieldnames=fieldnames) 
    writer.writeheader()
    for i in vaccination_records:
        writer.writerow(i)
print("CSV file saved successfully")