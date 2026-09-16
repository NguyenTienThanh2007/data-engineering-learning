'''Hãy:
Mở file vaccination_report.txt ở chế độ "w".
Dùng for duyệt từng dictionary.
Ghi mỗi record vào file theo mẫu:'''

'''Vietnam - 2024: 88.0%
Australia - 2025: 85.0%
Vietnam - 2025: 95.0%
Japan - 2025: 90.0%'''

'''Sau khi ghi xong, in:
Report saved successfully'''

vaccination_records = [
    {"country": "Vietnam", "year": 2024, "coverage": 88.0},
    {"country": "Australia", "year": 2025, "coverage": 85.0},
    {"country": "Vietnam", "year": 2025, "coverage": 95.0},
    {"country": "Japan", "year": 2025, "coverage": 90.0}
]
with open ("vaccination_report.txt", "w", newline = "") as file :
    for i in vaccination_records:
        file.write(f'{i['country']} - {i['year']}: {i['coverage']}%\n')
        