'''Tạo file dirty_vaccination_data.csv:

country,year,coverage
Vietnam,2025,95.0
Australia,wrong,85.0
Japan,2025,not_available
Thailand,2025,70.0
,2024,88.0

Có 3 dòng hợp lệ và 2 dòng lỗi số; dòng thiếu country cũng không hợp lệ.

Yêu cầu

Chương trình phải:

Đọc từng dòng bằng csv.DictReader.
Chuyển year sang int, coverage sang float.
Nếu không chuyển được, dùng except ValueError để bỏ qua.
Nếu country rỗng, bỏ qua.
Lưu record hợp lệ vào clean_records.
In số record hợp lệ và không hợp lệ.'''
import csv

clean_records = []
invalid_records = 0

with open("dirty_vaccination_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        country = row["country"]

        try:
            year = int(row["year"])
            coverage = float(row["coverage"])

        except ValueError:
            print(f"Skipped invalid row: {row}")
            invalid_records += 1
            continue

        if country == "":
            print(f"Skipped missing country: {row}")
            invalid_records += 1
            continue

        record = {
            "country": country,
            "year": year,
            "coverage": coverage
        }

        clean_records.append(record)


print("\n=== Cleaning Summary ===")
print(f"Valid records: {len(clean_records)}")
print(f"Invalid records: {invalid_records}")