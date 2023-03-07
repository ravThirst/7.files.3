import codecs
import os

folder_path = os.path.dirname(os.path.abspath(__file__))

files = os.listdir(folder_path)

file_lines = {}
for file_name in list(filter(lambda x: ".txt" in x and "result.txt" not in x, files)):
    with codecs.open(file_name, 'r', 'utf-8') as f:
        file_lines[file_name] = len(f.readlines())

sorted_file_lines = sorted(file_lines.items(), key=lambda x: x[1])

with codecs.open("result.txt", "w", 'utf-8') as result_file:
    for file_name, num_lines in sorted_file_lines:
        result_file.write(f"{file_name}\n{num_lines}\n")
        with codecs.open(file_name, 'r', 'utf-8') as f:
            result_file.write(f.read() + "\n")