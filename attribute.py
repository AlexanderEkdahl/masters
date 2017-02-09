import csv


class Attribute(object):
    """Attribute holds information for a specific type of attributes"""

    def __init__(self, name, compare_type, values):
        self.name = name
        self.compare_type = compare_type
        self.values = values

    def evaluate(self, attribute_value_a, attribute_value_b):
        """This method evaluates the result of this attribute given attribute_value_a and
        attribute_value_b"""

        if attribute_value_a is None or attribute_value_b is None:
            return False
        elif self.compare_type == 1:
                return attribute_value_a == attribute_value_b
        elif self.compare_type == 2:
            try:
                a = float(attribute_value_a)
                b = float(attribute_value_b)
                return attribute_value_a <= attribute_value_b
            except:
                pass
        elif self.compare_type == 3:
            try:
                a = float(attribute_value_a)
                b = float(attribute_value_b)
                return attribute_value_a >= attribute_value_b
            except:
                pass
        else:
            raise Exception("Unknown attribute type: %s" % self.compare_type)

    def __str__(self):
        return "Attribute: %s %s" % (self.name, self.compare_type)

    __repr__ = __str__


def load_attributes(input_file):
    """Load attributes from a csv, returns attributes as a list"""

    attributes = []
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            attributes.append(Attribute(row[0], int(row[2]), row[1]))

    return attributes
