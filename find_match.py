def find_match(model, product_a_id, range):
	scores = []

	for product_b in model.products:
		new_score = model.score(product_a_id, product_b)
		scores.append((new_score, product_b))
		scores.sort(key=lambda tup: -tup[0])
		scores = scores[:range]
	return scores
