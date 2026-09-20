'''Yêu cầu

Viết chương trình có 3 function:

extract_data(filename)
Đọc file CSV.
Trả toàn bộ các dòng dữ liệu về dạng list.
transform_data(records)
Xóa khoảng trắng ở country.
Chuyển year, target_population, doses_given sang int.
Dùng try/except xử lý dữ liệu không chuyển được thành số.
Record không hợp lệ nếu:
country rỗng.
target_population <= 0.
doses_given < 0.
Tính:
coverage = doses_given / target_population × 100
Làm tròn coverage 2 chữ số.
Thêm status:
Coverage từ 90 trở lên: High
Coverage từ 70 đến dưới 90: Medium
Coverage dưới 70: Low
Đếm số record không hợp lệ.
Trả dữ liệu sạch và số record lỗi.
load_data(records, filename)
Ghi dữ liệu sạch vào clean_vaccination_data.json.
JSON phải dễ đọc và hỗ trợ tiếng Việt.
Kết quả hợp lệ

Chỉ có 3 record hợp lệ:

[
    {
        "country": "Vietnam",
        "year": 2025,
        "target_population": 1000,
        "doses_given": 950,
        "coverage": 95.0,
        "status": "High"
    },
    {
        "country": "Australia",
        "year": 2025,
        "target_population": 2000,
        "doses_given": 1700,
        "coverage": 85.0,
        "status": "Medium"
    },
    {
        "country": "Canada",
        "year": 2024,
        "target_population": 800,
        "doses_given": 600,
        "coverage": 75.0,
        "status": "Medium"
    }
]
Kết quả Terminal
=== ETL Summary ===
Valid records: 3
Invalid records: 3
Saved to clean_vaccination_data.json
Điều kiện hoàn thành
Có đủ 3 function.
Có try/except.
Không bị lỗi chia cho 0.
File JSON chỉ chứa record hợp lệ.
Coverage và status phải đúng.
Không viết toàn bộ chương trình vào một khối duy nhất.'''