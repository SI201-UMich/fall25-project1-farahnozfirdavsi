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

# helping safe function to convert strings into floats
# so that we could calculate better
def safe_float(value):
    try:
        val = float(value)
        return val
    except (ValueError, TypeError):
        return None
    
# Farah's functions
def avg_body_mass_by_species_and_sex(data):
    results = {}
    for row in data:
        species = row.get("species", "")
        sex = row.get("sex", "")
        body_mass = safe_float(row.get("body_mass_g", ""))
        if not in species or not sex or body_mass is None:
            continue
        key = (species, sex)
        if key not in results:
            results[key] = {"total": 0, "count": 0}
        results[key]["total"] += body_mass
        results[key]["count"] += 1
    avg = {f"{sp} {{sx}}": roung(v["total"] / v["count"], 2) 
           for (sp, sx), v in results.items()}
    return avg

def avg_bill_lengh_by_island_and_year(data):
    results = {}
    for row in data:
        island = row.get("island", "")
        year = row.get("year", "")
        bill_length = safe_float(row.get("bill_length_mm", ""))
        if not island or not year or bill_length is None:
            continue
        key = (island, year)
        if key not in results:
            results[key] = {"total": 0, "count": 0}
        results[key]["total"] += bill_length
        results[key]["count"] += 1
    avg = {f"{is} {yr}": round(v["total"] / v["count"], 2) 
           for (is, yr), v in results.items()}
    return avg