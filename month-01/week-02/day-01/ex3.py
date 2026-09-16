'''Yêu cầu người dùng nhập:

Country
Year
Coverage

Sau đó thêm record mới vào cuối file vaccination_report.txt.

Ví dụ nhập:

Enter country: Thailand
Enter year: 2025
Enter coverage: 75

File sẽ được thêm dòng:

Thailand - 2025: 75.0%'''

country = input("Enter country: ")
year = int(input("Enter year: "))
coverage = float(input("Enter coverage: "))
if coverage < 0:
    print("Invalid")
else:
    with open ("vaccination_report.txt", "a" ) as file :
        file.write(f'{country} - {year} : {coverage} %\n ')
    with open ("vaccination_report.txt", "r") as file :
        line = file.readlines()
    print("===Summary===")
    for i in line:
        print(i.strip())
        
        
        
    
    
    
    
    