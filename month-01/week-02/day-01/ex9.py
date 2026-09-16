'''Bài tập: Đếm số record theo status

Đọc file vừa tạo:

vaccination_with_status.csv

Đếm xem có bao nhiêu record thuộc mỗi nhóm:

High
Medium
Low

Kết quả mong muốn:

=== Status Summary ===
High: 2
Medium: 2
Low: 1
Total records: 5'''
import csv
status_count = {
    
    
}
count_high = 0 
count_medium = 0
count_low = 0
total_records = 0
with open("vaccination_with_status.csv", "r" ) as file :
    reader = csv.DictReader(file)
    for i in reader :
        country = i["country"]
        year = int(i["year"])
        coverage = float(i["coverage"])
        status = i['status']
        if status.lower() == "high":
            count_high += 1
        if status.lower() == "medium":
            count_medium+=1
        if status.lower() == "low":
            count_low += 1 
        total_records += 1 
print ("===Status Summary===")
print(f'High: {count_high}')
print(f'Medium: {count_medium}')
print(f'Low: {count_low}')
print(f'Total records: {total_records}')


                
            
                
        