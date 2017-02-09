import csv


class AttributeException(Exception):
    pass


class Attribute(object):
    """Attribute holds information for a specific type of attributes"""

    def __init__(self, name, compare_type, values):
        self.name = name
        self.compare_type = compare_type
        self.values = values

    def rewrite_attribute_value(self, attribute_value):
        """Rewrites the value from the list of available values"""
        if attribute_value is None:
            return None

        try:
            return self.values.index(attribute_value)
        except ValueError:
            print("%s not found in %s" % (attribute_value, self))
            return None

    def evaluate(self, attribute_value_a, attribute_value_b):
        """This method evaluates the result of this attribute given attribute_value_a and
        attribute_value_b"""

        if attribute_value_a is None or attribute_value_b is None:
            return False
        elif self.compare_type == 1:
            return attribute_value_a == attribute_value_b
        else:
            raise AttributeException(
                "Unknown attribute type: %s" % self.compare_type)

    def __str__(self):
        return "Attribute: %s %s %s" % (self.name, self.compare_type, self.values)

    __repr__ = __str__


def load_attributes(input_file):
    """Load attributes from a csv, returns attributes as a list"""

    attributes = []
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            attributes.append(
                Attribute(row[0], int(row[2]), row[1].split(",")))

    return attributes
