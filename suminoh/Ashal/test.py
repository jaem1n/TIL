def select_high_scores(scores, base_score):
    high_scores = []

    for score in scores:
        if score >= base_score:
            high_scores.append(score)

    return high_scores