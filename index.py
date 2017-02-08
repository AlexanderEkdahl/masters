import product
import match
import split
import simple_model
import attribute
import validate
import find_match

def train_and_evaluate_simple_model():
    """Runs the simple training model for data residing in the data folder"""
    products = product.load_products("./data/products.csv")
    attributes = attribute.load_attributes("./data/attributes.csv")
    matches = match.load_matches("./data/matches.csv")
    (train, test) = split.split_train_test(matches)

    model = simple_model.SimpleModel(products, attributes)
    model.train(train)

    validate.validate_model(model, test)
    # print(find_match.find_match(model, 31140))
    print(find_match.find_match(model, 33795))
    # print(find_match.find_match(model, 49031))


if __name__ == '__main__':
    train_and_evaluate_simple_model()
