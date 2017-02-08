"""This file holds code for parsing match data"""

import csv

def load_matches(input_file):
    """Load matches from input_file"""

    matches = []
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            matches.append((int(row[0]), int(row[1])))

    return matches
