'''Đọc file:
vaccination_data.json
Chọn các record có:
coverage >= 90
Sau đó lưu vào file mới:
high_coverage.json
Ví dụ dữ liệu đầu vào:
[
    {
        "country": "Vietnam",
        "year": 2025,
        "coverage": 95.0
    },
    {
        "country": "Thailand",
        "year": 2025,
        "coverage": 70.0
    }
]
Kết quả trong high_coverage.json:
[
    {
        "country": "Vietnam",
        "year": 2025,
        "coverage": 95.0
    }
]'''
import json
high_coverage = []
with open ("vaccination_data.json", "r", encoding="utf-8") as input_file:
    data = json.load(input_file)
    for i in data:
        if i["coverage"] >= 90 :
            high_coverage.append(i)

with open ("high_coverage.json", "w", encoding="utf-8") as output_file:
    json.dump(high_coverage, output_file, indent=4, ensure_ascii=False)
print(f"Saved records: {len(high_coverage)}")
print(f"Saved to high_coverage.json")

        