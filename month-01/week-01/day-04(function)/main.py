'''Viết chương trình có 3 function:

calculate_coverage(doses_given, target_population)
Tính tỷ lệ tiêm chủng.
Làm tròn 2 chữ số.
Trả kết quả bằng return.
get_status(coverage)
Nhận coverage.
Trả về trạng thái phù hợp.
print_report(country, year, coverage, status)
In báo cáo hoàn chỉnh.
Function này chỉ cần print(), không cần return.'''

'''== Vaccination Report ==
Country: Vietnam
Year: 2025
Coverage: 95.0%
Status: Excellent coverage'''

def calculate_coverage(doses_given, target_population):
    coverage = round((doses_given/target_population*100),2)
    return coverage
def get_status(coverage):
    if coverage > 100:
        return "Review required"
    elif coverage >= 90:
        return "Excellent coverage"
    elif coverage >= 80:
        return "Good coverage"
    elif coverage >= 50:
        return "Needs improvement"
    else:
        return "Critical coverage"
def print_report(country, year, coverage, status):
    print(f'\n ===Vaccination Report===')
    print(f'Country: {country}')
    print(f'Year: {year}')
    print(f'Coverage: {coverage}')
    print(f'Status: {status}')
country = input("Enter country:")
year = int(input("Enter year: "))
doses_given = int(input("Enter doses given: "))
target_population = int(input("Enter target population: "))
if doses_given < 0:
    print("Invalid")
elif target_population < 0 :
    print("Invalid")
else:
    coverage = result 
    status = get_status(coverage)
    print_report(country, year, coverage, status)
    
