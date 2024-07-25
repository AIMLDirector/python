import csv
with open('state_us.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row["State"]} short name is {row["Abbreviation"]} ')
            line_count += 1
    print(f'Processed {line_count} lines.')

