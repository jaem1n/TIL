scores = [80,100,70,90,40]

def total_score(scores):
    total_score = 0
    for i in range(0,len(scores)):
        total_score += scores[i]
    return total_score

print("Total score:", total_score(scores))

def avg_score(scores):
    return total_score(scores) / len(scores)

print("Average score:", avg_score(scores))
