
def total(scores):
    acc = 0
    for i in range(0, len(scores)):
        acc += scores[i]
    return acc

print(total([80, 100, 70, 90, 40]))


def pyeong(scores):
    acc = 0
    for i in range(0, len(scores)):
        acc += scores[i]
    return acc / len(scores)

print(pyeong([80, 100, 70, 90, 40]))

# 1234