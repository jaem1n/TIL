
def total(scores):
    total_score = 0
    for i in range(len(scores)):
        total_score += scores[i]
    return total_score

def average(scores):
    return total(scores) / len(scores)

print('총점:', total([80, 100, 70, 90, 40]))
print('평균:', average([80, 100, 70, 90, 40]))


def total(scores):
    acc = 0
    for i in range(0, len(scores)):
        acc += scores[i]
    return acc

# +print(total([80, 100, 70, 90, 40]))
# +
# +
# +def pyeong(scores):
# +    acc = 0
# +    for i in range(0, len(scores)):
# +        acc += scores[i]
# +    return acc / len(scores)