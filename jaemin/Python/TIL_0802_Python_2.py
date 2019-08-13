# < 계승 구하기 >

# 입력
n = 3

# 계산
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# 출력
print(factorial)



# < 성적 총합 & 평균 구하기 >

my_scores = [30, 90, 80, 40, 50]

sum_m = 0
for i in my_scores:
    sum_m += i

avg_m = sum_m/len(my_scores)

print(sum_m)
print(avg_m)

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

class_scores_sum = []
class_scores_avg = []
for i in range(0,3):
    class_scores_sum.append(sum(class_scores[i]))
    class_scores_avg.append(sum(class_scores[i])/len(class_scores[i]))

sum_c = sum(class_scores_sum)
avg_c = sum(class_scores_avg)/len(class_scores_avg)

print(sum_c)
print(avg_c)



# < 구구단 출력하기 >

for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d" % (i,j,i*j))

for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)