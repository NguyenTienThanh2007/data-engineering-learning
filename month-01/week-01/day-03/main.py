'''Hỏi người dùng muốn nhập bao nhiêu bản ghi.
Dùng vòng lặp for để nhập từng bản ghi:
Quốc gia
Năm
Dân số mục tiêu
Số liều đã tiêm
Kiểm tra dữ liệu:
target_population phải lớn hơn 0.
doses_given không được âm.
Nếu dữ liệu sai, dùng continue để bỏ qua bản ghi.
Tính tỷ lệ bao phủ.
Phân loại trạng thái.
Cuối cùng in:
Số bản ghi hợp lệ.
Tỷ lệ bao phủ trung bình.'''

num_records = int(input('Enter the number of records: '))
total_records = 0 
total_coverage = 0 
for i in range(1, num_records+1):
    print(f'\n ==Records: {i}==')
    country = input("Enter your country: ")
    year = int(input("Enter year: "))
    target_population = int(input("Enter target population: "))
    doses_given = int(input("Enter doses given: "))
    if target_population <= 0:
        print('Invalid')
        continue
    if doses_given < 0:
        print('Invalid')
        continue
    coverage = round((doses_given / target_population) * 100, 2)
    
    if coverage>100:
        status = "Review required"
    elif coverage >= 90:
        status = "Excellent coverage"
    elif coverage >= 80:
        status = "Good coverage"
    elif coverage >= 50:
        status = "Needs improvement"
    else:
        status = "Critical coverage"
    
    print(f'Country: {country}')
    print(f'Year: {year}')
    print(f'Coverage: {coverage}%')
    print(f'Status: {status}')
    total_records += 1
    total_coverage += coverage
    
if total_records > 0:
    avg_coverage = round(total_coverage / total_records, 2)
    print(f'Summary')
    print(f'Valid records: {total_records}')
    print(f'Average coverage: {avg_coverage}%')
        
        
        
 
    
   
    
    
    
    
    