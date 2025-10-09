import csv

# -----------------------------------------------------
# 1. Load CSV
# -----------------------------------------------------
def load_csv(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if '' in row:
                del row['']
            data.append(row)
    return data
# helper to convert strings to floats safely
def safe_float(value):
    """Convert string to float, safely skipping bad or missing values."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None