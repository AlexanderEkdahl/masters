"""This file holds the product class and the code for loading a csv of products"""

import csv
import json


class Product(object):
    """"""

    def __init__(self, product_id, name, feature_values):
        self.product_id = product_id
        self.name = name
        self.feature_values = feature_values

    def __str__(self):
        return "%s: %s" % (self.product_id, self.name)

    __repr__ = __str__


def load_products(input_file):
    """Load products from a csv"""

    products = {}
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            product_id = int(row[0])
            products[product_id] = Product(product_id, row[1], json.loads(row[2]))

    return products
