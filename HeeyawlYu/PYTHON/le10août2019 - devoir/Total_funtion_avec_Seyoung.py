

def total(scores):
    total_scores = 0
    for i in range(0,len(scores)):
        total_scores += scores[i]
    return total_scores


assert total([80]) == 80
assert total([20, 80]) == 20 + 80

Seyoung = [1, 2, 3, 4, 5]
assert total(Seyoung) == 15

def gobagi(scores):
    total_scores = 1
    for i in range(0,len(scores)):
        total_scores *= scores[i]
    return total_scores

assert gobagi(Seyoung) == 120