def chong(scores):
    acc = 0
    for i in range(0, len(scores)):
        acc += scores[i]
    return acc


print(chong([80, 100, 70, 90, 40]))


def pyeong(scores):
    return chong(scores) / len(scores)


print(pyeong([80, 100, 70, 90, 40]))
