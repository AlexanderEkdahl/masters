class SimpleModel(object):

    def __init__(self, products, attributes):
        self.products = products
        self.attributes = attributes
        self.weighs = None

    def train(self, matches):
        count_matches = [0] * len(self.attributes)

        for (product_a_id, product_b_id) in matches:
            try:
                product_a = self.products[product_a_id]
                product_b = self.products[product_b_id]

                for i, attribute in enumerate(self.attributes):
                    if attribute.evaluate(product_a.feature_values[i],
                                          product_b.feature_values[i]):
                        count_matches[i] += 1
            except KeyError:
                # Product from match was not found in products
                pass

        weigh_sum = sum(count_matches)
        self.weighs = [x / weigh_sum for x in count_matches]

    def score(self, product_a_id, product_b_id):
        try:
            product_a = self.products[product_a_id]
            product_b = self.products[product_b_id]
        except KeyError:
            return False

        result = 0

        for i, attribute in enumerate(self.attributes):
            if attribute.evaluate(product_a.feature_values[i],
                                  product_b.feature_values[i]):
                result += self.weighs[i]

        return result
