'''Bài tập Pathlib 1

Tạo cấu trúc:

pathlib-practice/
├── main.py
└── data/
    └── vaccination_data.csv

Nội dung CSV:

country,year,coverage
Vietnam,2025,95
Australia,2025,85
Canada,2024,75

Trong main.py, hãy:

Import Path.
Lấy thư mục chứa main.py và lưu vào base_dir.
Tạo đường dẫn tới thư mục data.
Tạo đường dẫn tới vaccination_data.csv.
In cả ba đường dẫn.
Kiểm tra CSV có tồn tại không.
Tạo thư mục output.
In "Ready to process data" nếu CSV tồn tại.
In "Input file not found" nếu không tồn tại.

Kết quả mong muốn:

Base directory: ...
Data directory: ...
Input file: ...
Input file exists
Output directory created
Ready to process data'''
from pathlib import Path


# Lấy thư mục đang chứa file main.py
base_dir = Path(__file__).parent

# Tạo đường dẫn đến thư mục data
data_dir = base_dir / "data"

# Tạo đường dẫn đầy đủ đến file CSV
input_file = data_dir / "vaccination_data.csv"

# Tạo đường dẫn đến thư mục output
output_dir = base_dir / "output"


print(f"Base directory: {base_dir}")
print(f"Data directory: {data_dir}")
print(f"Input file: {input_file}")


# Kiểm tra file CSV có tồn tại không
if input_file.exists():
    print("Input file exists")
else:
    print("Input file not found")


# Tạo thư mục output nếu chưa tồn tại
output_dir.mkdir(exist_ok=True)

print(f"Output directory: {output_dir}")
print("Output directory created")


# Chỉ xử lý dữ liệu nếu file đầu vào tồn tại
if input_file.exists():
    print("Ready to process data")
else:
    print("Cannot process data because input file does not exist")
