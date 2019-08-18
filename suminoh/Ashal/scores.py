# def total_all(scores):
#     total = 0
#     for i in range(len(scores)):
#         for j in scores[i]:
#             total += scores[i][j]
#     return total

def total_class(scores, subject):
    total = 0
    for i in range(len(scores)):
        total += scores[i][subject]
    return total
