def find_match(model, product_a_id):
    max_score_and_product_id = (0, None)

    for product_b in model.products:
        new_score = model.score(product_a_id, product_b)

        if new_score > max_score_and_product_id[0]:
            max_score_and_product_id = (new_score, product_b)

    return max_score_and_product_id
