'''Đọc file vaccination_report.txt và:

In toàn nội dung file.
In mỗi từng in mỗi dòng riêng biệt.
Đếm file có bao nhiêu dòng dữ liệu.'''

'''Vietnam - 2024: 88.0%
Australia - 2025: 85.0%
Vietnam - 2025: 95%
Japan - 2025: 90.0%

Total records: 4'''
with open ("vaccination_report.txt", "r", newline = "") as file :
    reader = file.readlines()
    
    print("===Summary===\n")
    for i in reader : 
        print(i.strip())
        
print(f'\nTotal records: {len(reader)}')
    
    
    
    
