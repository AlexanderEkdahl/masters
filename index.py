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

    test_matches = []
    for _ in range(10):
        test_matches.append(test.pop())

    precision = 10
    for original, new in test_matches:
        if new in [x[1] for x in find_match.find_match(model, original, precision)]:
            print(str(original) + " found correct match " + str(new) + " within top " + str(precision) + " matches") 
        else:
            print("Nope")


if __name__ == '__main__':
    score = train_and_evaluate_simple_model()
