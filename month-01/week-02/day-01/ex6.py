'''Yêu cầu:

Mở file bằng chế độ "r".
Dùng csv.reader(file).
Bỏ qua header bằng next(reader).
Tạo:
total_coverage = 0
total_records = 0
highest_coverage = None
highest_country = None
Duyệt từng row.
Đổi coverage từ chuỗi sang float.
Cộng coverage vào tổng.
Tìm coverage và country cao nhất.
Sau vòng lặp, tính coverage trung bình.
In kết quả.'''

'''Kết quả cần đạt:

=== Summary ===
Average coverage: 89.5%
Highest coverage: 95.0%
Country with highest coverage: Vietnam'''
import csv
total_records = 0
total_coverage = 0
highest_coverage = None
highest_country = None
with open ("vaccination_data.csv", "r", newline = "") as file :
    reader = csv.reader(file)
    header = next(reader)
    for i in reader :
        country = i[0]
        year = i[1]
        coverage = float(i[2])
        total_coverage += coverage
        total_records += 1 
        
        if highest_coverage is None or highest_coverage < coverage:
            highest_coverage = coverage
            highest_country = i[0]
if total_records > 0 :
    print(f'===Summary===')
    print(f'Average coverage: {round((total_coverage/ total_records), 2)}')
    print(f'Highest coverage: {highest_coverage}')
    print(f'Country with the highest coverage: {highest_country}')
else:
    print("No records")

            
        
        
    
    
