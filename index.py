"""Main file for training and evaluating model performance"""

import sys
import product
import match
import split
import simple_model
import attribute
import validate


def train_and_evaluate_simple_model():
    """Runs the simple training model for data residing in the data folder"""
    attributes = attribute.load_attributes("./data/cellphone_attributes.csv")
    products = product.load_products("./data/cellphones.csv", attributes)
    matches = match.load_matches("./data/matches.csv", products)
    (train, test) = split.split_train_test(matches, 0.3)

    model = simple_model.SimpleModel(products, attributes)
    model.train(train)
    print("Average score: %s" % validate.average_score(model, test))
    print("MSE: %s" % validate.mean_squared_error(model, test[:40]))


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Requires Python 3+")

    train_and_evaluate_simple_model()
