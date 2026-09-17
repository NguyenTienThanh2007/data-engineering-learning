'''Bạn đang có file dirty_vaccination_data.csv:

country,year,coverage
Vietnam,2025,95.0
Australia,wrong,85.0
Japan,2025,not_available
Thailand,2025,70.0
,2024,88.0

Trong đó:

Australia sai vì year = wrong.
Japan sai vì coverage = not_available.
Dòng cuối sai vì thiếu country.
Vietnam và Thailand hợp lệ.
Yêu cầu

Viết chương trình thực hiện 2 phần:

Đọc và làm sạch dữ liệu:
Bỏ qua dòng có year hoặc coverage không chuyển được thành số.
Bỏ qua dòng không có country.
Thêm các dòng hợp lệ vào clean_records.
Ghi dữ liệu sạch vào file mới:
clean_vaccination_data.csv

File kết quả phải là:

country,year,coverage
Vietnam,2025,95.0
Thailand,2025,70.0

Cuối cùng in:

=== Cleaning Summary ===
Valid records: 2
Invalid records: 3
Saved to clean_vaccination_data.csv'''
import csv 
clean_records = []
invalid_records = 0
with open ("dirty_vaccination_data.csv", "r", newline = "") as input_file:
    reader = csv.DictReader(input_file)
    for i in reader :
        country = i["country"].strip()
        try:
            year = int(i["year"])
            coverage = float(i["coverage"])
        except ValueError :
            print(f"Skipped error row : {i}")
            invalid_records += 1
            continue
        if country.strip() == "":
            print(f"Skipped error row: {i}")
            invalid_records += 1 
            continue
        record = {
            "country" : country,
            "year" : year,
            "coverage" : coverage
            
        }
        clean_records.append(record)
with open ("clean_vaccination_data.csv", "w", newline = "") as output_file:
    fieldnames = ["country", "year", "coverage"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    for j in clean_records:
        writer.writerow(j)
        
print("====Cleaning Summary===")
print(f"Valid records: {len(clean_records)}")
print(f"Invalid_records: {invalid_records}")
print("Saved to clean_vaccination_data.csv")
        
        
    
    
        
            