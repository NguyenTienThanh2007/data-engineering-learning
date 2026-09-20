'''Yêu cầu
Viết chương trình:

Đọc vaccination_data.json.
Tạo function:
calculate_summary(records)
Function phải tính:
Tổng số record.
Coverage trung bình, làm tròn 2 chữ số.
Coverage cao nhất.
Country có coverage cao nhất.
Function trả về một dictionary chứa kết quả.
Ghi dictionary kết quả vào summary.json.
In kết quả ra Terminal.
Kết quả mong muốn

File summary.json:
{
    "total_records": 4,
    "average_coverage": 85.0,
    "highest_coverage": 95.0,
    "highest_country": "Vietnam"
}
Terminal:
=== Vaccination Summary ===
Total records: 4
Average coverage: 85.0%
Highest coverage: 95.0%
Highest country: Vietnam
Saved to summary.json
Điều kiện hoàn thành
Phải dùng json.load() để đọc.
Phải có function calculate_summary(records).
Function phải dùng return.
Phải dùng json.dump() để ghi summary.json.
Nếu danh sách rỗng, không được chia cho 0.'''
import json 
with open ("vaccination_data.json", "r", encoding= "utf-8") as input_file :
    data = json.load(input_file) 
def calculate_summary (records):
    total_records = len (records)
    if total_records == 0:
        return {
            "total_records": 0,
            "average_coverage": 0,
            "highest_coverage": 0,
            "highest_country": None 
            
        }
    total_coverage = 0 
    highest_records = records[0]
    for i in records :
        total_coverage += i["coverage"]
        if highest_records["coverage"] <= i["coverage"]:
            highest_records = i
    average_coverage = round((total_coverage/ total_records), 2)
    summary = {
        "total_records": total_records,
        "average_coverage": average_coverage,
        "highest_coverage": highest_records["coverage"],
        "highest_country": highest_records["country"]
    }
    return summary 
summary = calculate_summary(data)
    
with open ("summary.json", "w", encoding = "utf-8") as output_file:
    json.dump (summary, output_file, indent=4, ensure_ascii=False )
print ("===Vaccination Summary==")
print(f"Total records: {summary["total_records"]}")
print(f"Average coverage: {summary["average_coverage"]}")
print(f"Highest country:{summary["highest_country"]} ")
print(f"Saved to summary.json")
    
    
