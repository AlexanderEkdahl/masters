"""This modules validates a model and returns comparable metrics"""

import find_match


def average_score(model, matches):
    """Returns the average score from all the matches"""
    scores = []

    for (product_a_id, product_b_id) in matches:
        score = model.score(product_a_id, product_b_id)
        scores.append(score)

    result = sum(scores) / max(len(scores), 1)
    return result


def positions(model, matches):
    """Returns the position that a match was found at given matches"""
    result = []

    for original, new in matches:
        index = find_match.find_all_matches(model, original).index(new)
        result.append(index)

    return result


def mean_squared_error(model, matches):
    """Returns the average distance squared. Penalizing bigger misstakes more"""
    positions_list = positions(model, matches)
    return sum([x ** 2 for x in positions_list]) / max(len(positions_list), 1)
