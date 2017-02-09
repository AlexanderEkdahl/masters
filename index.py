"""Main file for training and evaluating model performance"""

import sys
import product
import match
import split
import simple_model
import attribute
import validate
import find_match


def train_and_evaluate_simple_model():
    """Runs the simple training model for data residing in the data folder"""
    attributes = attribute.load_attributes("./data/attributes.csv")
    products = product.load_products("./data/products.csv", attributes)
    matches = match.load_matches("./data/matches.csv")
    (train, test) = split.split_train_test(matches)

    model = simple_model.SimpleModel(products, attributes)
    model.train(train)
    print("Average score: %s" % validate.validate_model(model, test))

    test_matches = []
    for _ in range(10):
        test_matches.append(test.pop())

    for original, new in test_matches:
        index = find_match.find_all_matches(model, original).index(new)
        print("The match for %s was %s and was found at position %s" %
              (original, new, index))


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Requires Python 3+")

    train_and_evaluate_simple_model()
