import csv
import sys
import re

def clean_header(header):
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", header.strip().lower())
    return re.sub(r"_+", "_", clean).strip("_")

def clean_row(row):
    return [cell.strip() if cell else "" for cell in row]

def process(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8", newline="") as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        headers = next(reader, None)
        if headers:
            writer.writerow([clean_header(h) for h in headers])
        for row in reader:
            writer.writerow(clean_row(row))

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        process(sys.argv[1], sys.argv[2])
