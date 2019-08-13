scores = [80, 100, 70, 90, 40]

# 총합 구하기
def total(scores):
    total_score=0
    for i in range(0, len(scores)):
        total_score += scores[i]
    return total_score

print(total(scores))

# total 함수 다시 활용하기

def average(scores):
    return total(scores)/len(scores)

print(average(scores))

# total 함수 활용하지 않고 Average 함수 만들기

def average(scores):
    total_score = 0
    for i in range(0, len(scores)):
        total_score += scores[i]
    return total_score/len(scores)

print(average(scores))
