## Script to change csv file encodings ##
import csv
from pathlib import Path

def convert_csv_to_utf8(input_file_dir, output_file_dir, current_encoding):
    with open(input_file_dir, 'r', encoding=current_encoding) as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]

    with open(output_file_dir, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
    
def conver_files(raw_string_data_dir):
    # Specify the input and output file paths - input must be raw string
    data_dir = Path(raw_string_data_dir)
    output_dir = data_dir / "modified_encodings"
    files = [f.name for f in data_dir.glob("*.csv")]
    # Specify the current encoding of the input file
    current_encoding = 'ANSI'

    for file in files:
        convert_csv_to_utf8(input_file_dir = data_dir / file,
                            output_file_dir = output_dir / file,
                            current_encoding = current_encoding)