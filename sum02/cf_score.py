scores = [80, 100, 70, 90, 40]

def total(scores):
    total_sum = 0
    for i in range(0, len(scores)):
        total_sum += scores[i]
    return total_sum
print(total(scores))

def avg(scores):
    total_sum = 0
    for i in range(0, len(scores)):
        total_sum += scores[i]
    total_avg = total_sum / len(scores)
    return total_avg
print(avg(scores))

"""
190806 
total 함수를 호출하는 avg2 함수 만들기
더 훌륭한 함수가 되었어요!!!
"""

def avg2(scores):
    avg2 = total(scores) / len(scores)
    return avg2
print(avg2(scores))