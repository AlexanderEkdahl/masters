def find_match(model, product_a_id, range):
    top_matches = []

    for product_b in model.products:
        new_score = model.score(product_a_id, product_b)
        if len(top_matches) > 0 and new_score > top_matches[-1][1]:
            top_matches.append((new_score, product_b))
            top_matches.sort(key=lambda tup: -tup[0])
            top_matches = top_matches[:range]
        else:
            top_matches.append((new_score, product_b))

    return top_matches

def find_all_matches(model, product_a_id):
    """Returns all products that matches product_a_id in descending order"""
    matches = []

    for product_b_id in model.products:
        score = model.score(product_a_id, product_b_id)
        matches.append((score, product_b_id))

    matches.sort(key=lambda x: -x[0])

    return [x[1] for x in matches]
