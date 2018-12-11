import csv
import sys
valid_lines = 0
invalid_lines = 0
all_lines = 0
lines = []
with open('data/oddetect.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        valid_lines += 1
        if len(row) == 14:
            for i in range(len(row)):
                row[i] = row[i].strip()
            lines.append(row)
        else:
            sys.stderr.write(f"warning {str(row)}\n")
            invalid_lines += 1
            continue


with open('data/fixed.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()

print(f"valid lines: {valid_lines} invalid lines: {invalid_lines}")