'''Đọc file:
clean_vaccination_data.csv
Chuyển toàn bộ dữ liệu sang file:
vaccination_data.json
Kết quả mong muốn:
[
    {
        "country": "Vietnam",
        "year": 2025,
        "coverage": 95.0
    },
    {
        "country": "Thailand",
        "year": 2025,
        "coverage": 70.0
    }
]'''
import csv
import json
vaccination_data_records = []
with open ("clean_vaccination_data.csv", "r", newline= "") as input_file:
    reader = csv.DictReader(input_file)
    for i in reader:
        country = i["country"].strip()
        year = int(i["year"])
        coverage = float(i["coverage"])
        record = {
            "country" : country,
            "year" : year,
            "coverage" : coverage
        }
        vaccination_data_records.append(record)
print(vaccination_data_records)
with open ("vaccination_data.json", "w", newline="") as output_file:
    json.dump(vaccination_data_records, output_file, indent=4)
print(f"Saved records: {len(vaccination_data_records)}")
print("Saved to vaccination_data.json")

                   