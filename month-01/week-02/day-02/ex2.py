'''Viết chương trình có 3 function:

extract_data(filename)
Đọc dữ liệu từ file JSON.
Trả dữ liệu ra ngoài.
transform_data(records, minimum_coverage)
Nhận danh sách record và mức coverage tối thiểu.
Chỉ giữ record có coverage >= minimum_coverage.
Trả danh sách đã lọc.
load_data(records, filename)
Ghi danh sách record vào file JSON mới.
JSON phải được trình bày dễ đọc.

Chương trình chính phải:

Đọc vaccination_data.json.
Lọc với mức coverage tối thiểu là 90.
Ghi kết quả vào high_coverage.json.
In số record đã lưu.
Kết quả mong muốn
Saved records: 2
Saved to high_coverage.json

File high_coverage.json chỉ chứa Vietnam và Japan.'''
import json


def extract_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def transform_data(records, minimum_coverage):
    filtered_data = []

    for record in records:
        if record["coverage"] >= minimum_coverage:
            filtered_data.append(record)

    return filtered_data


def load_data(records, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


data = extract_data("vaccination_data.json")

filtered_data = transform_data(data, 90)

load_data(filtered_data, "high_coverage.json")

print(filtered_data)

        
