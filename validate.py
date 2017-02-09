def validate_model(model, matches):
    scores = []

    for (product_a_id, product_b_id) in matches:
        score = model.score(product_a_id, product_b_id)

        if score:
            scores.append(score)

    average_score = float(sum(scores)) / max(len(scores), 1)
    return average_score
