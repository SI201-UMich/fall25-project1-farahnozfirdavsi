import csv
import unittest

# loading the data
def load_data(penguins.csv):
    data = []
    with open (penguins.csv, "r", encoding="utf-8") as infile:
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            data.append(row)
    return data