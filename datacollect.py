import csv
from testsolver2 import*


def write_csv():
    with open('statistics.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open('statistics.csv', 'a') as f:
            fieldnames = ['Empty Blanks', 'Variable 1', 'Variable 2', 'Variable 3', 'Variable 4', 'Variable 5']
            writer = csv.writer(f, fieldnames= fieldnames, delimiter='\t')
            stats = str(variable_1) + str(variable_2)
            writer.writerow(stats)



