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
