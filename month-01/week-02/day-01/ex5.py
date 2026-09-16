'''Yêu cầu
Mở file ở chế độ "r".
Tạo reader bằng csv.reader(file).
Bỏ qua dòng tiêu đề bằng next(reader).
Duyệt từng dòng dữ liệu.
In country, year và coverage.
Đếm số record.'''
import csv 
total_records = 0 
with open ("vaccination_data.csv", "r", newline = "") as file :
    reader = csv.reader(file)
    header = next(reader)
    for i in reader: 
        country = i[0]
        year = i[1]
        coverage = i[2]
        print(f'{country} - {year} : {coverage}')
        total_records += 1 
print(f"Total records: {total_records}")

        

    
    
    