def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_scores = sorted(scores, reverse=True)
    if (len(sorted_scores) == 2):
        return [sorted_scores[0], sorted_scores[1]]
    elif (len(sorted_scores) == 1):
        return [sorted_scores[0]]
    else:
        return [sorted_scores[0], sorted_scores[1], sorted_scores[2]]
