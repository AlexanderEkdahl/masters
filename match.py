"""This file holds code for parsing match data"""

import csv

def load_matches(input_file, products):
    """Load matches from input_file"""

    matches = []
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            product_a_id = int(row[0])
            product_b_id = int(row[1])
            if product_a_id in products and product_b_id in products:
                matches.append((int(row[0]), int(row[1])))

    return matches
