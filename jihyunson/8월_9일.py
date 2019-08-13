'''score가 다음과 같은 형태:
scores = [80, 100, 70, 90, 40]
total, average를 만드려고 합니다.
 1. 테스트 코드 작성, 2. TDD 로 함수 만들기, 3. 코드를 GitHub에 올리기, 4. 코드 리뷰
'''

scores = [80, 100, 70, 90, 40]
def ta(scores):
    total_score = 0
    for i in range(len(scores)):
        total_score += scores[i]
    total_average = total_score/len(scores)
    return total_score, total_average
print ta(scores)