'''Yêu cầu

Chương trình phải:

Tạo list rỗng tên coverage_values.
Hỏi người dùng muốn nhập bao nhiêu bản ghi.
Dùng for để nhập từng bản ghi:
target_population
doses_given
Nếu target_population <= 0 hoặc doses_given < 0:
In "Invalid record".
Dùng continue bỏ qua bản ghi.
Tính coverage.
Dùng append() thêm coverage vào list.
Sau vòng lặp, in:
Toàn bộ coverage.
Số bản ghi hợp lệ.
Coverage trung bình.
Coverage cao nhất.
Coverage thấp nhất.'''

'''== Coverage List ==
95.0%
85.0%
60.0%

== Summary ==
Valid records: 3
Average coverage: 80.0%
Highest coverage: 95.0%
Lowest coverage: 60.0%'''

def calculate_coverage (target_population, doses_given):
    result = round((doses_given/target_population *100), 2)
    return result
coverage_values = [] 
record = int(input("Enter number records: "))
for i in range(1, record+1):
    print(f'Record: {i}')
    target_population = int(input("Enter target_population:"))
    doses_given = int(input("Enter doses given: "))
    if target_population <= 0:
        print("Invalid")
        continue
    if doses_given < 0 :
        print("Invalid")
        continue
    result = calculate_coverage (target_population, doses_given)
    coverage_values.append(result)

print(f'===Coverage List===')
for j in coverage_values :
    print(f'{j}%')
    
if len(coverage_values) > 0:
    avg = (sum(coverage_values)/len(coverage_values))
    print(f'\n===Summary===')
    print(f'Valid records: {i}')
    print(f'Average coverage: {avg}')
    print(f'Highest coverage: {max(coverage_values)}')
    print(f'Lowest coverage: {min(coverage_values)}')
else:
    print("Invalid")
    
    
    
        
    
    
    
    