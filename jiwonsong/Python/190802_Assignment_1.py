my_scores = [30, 90, 80, 40, 50]
class_scores = [[30, 90, 80, 40, 50],
                [100, 100, 100, 100, 100],
                [90, 90, 30, 30, 20]]

# 성적 총합 & 평균 구하기
## my_scores
total_score = 0
my_scores = [30, 90, 80, 40, 50]

for i in range(0, len(my_scores)):
    total_score += my_scores[i]
    average = total_score / len(my_scores)

print(total_score)
print(average)

## total_score
class_scores = [[30, 90, 80, 40, 50],
                [100, 100, 100, 100, 100],
                [90, 90, 30, 30, 20]]
total_score = 0
total_length = 0
for i in range(len(class_scores)):
    total_length = len(class_scores[i])
   for j in range(len(class_scores[i])):
       total_score += class_scores[i][j]
       average = sum/(len(class_scores)*total_length)
print(total_score)
print(average)



# 구구단 출력하기
for i in range(2,10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
    print("-"*20)


