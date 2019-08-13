# 190807 강의 내용 복습
def total(scores):
    total_score = 0
    for i in range(0,len(scores)):
            total_score += scores[i]
    return total_score

print(total([80,100,70,90,40]))
# 같은 이름은 사용하지 않는 것이 좋음

# 190805 코드
def total_score():
    return sum(scores)

print("Total score:", total_score())

def avg_score():
    return total_score() / len(scores)
print("Average score:", avg_score())


# 190805 코드 수정
def total_score(scores):
    total_score = 0

    # sum 함수 대신 for문 사용
    for i in range(0,len(scores)):
        total_score += scores[i]
    return total_score

# 함수에 입력이 있도록.
print("Total score:", total_score(scores))

def avg_score(scores):
    return total_score(scores) / len(scores)
print("Average score:", avg_score(scores))


# 입력과 출력이 명확하도록.