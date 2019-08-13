scores=[80, 100, 70, 90, 40]

num=len(scores)

def total(n):
    sum = 0
    for i in n:
        sum += i
    return sum

def average(m):
    avg = total(m)/num
    return avg

print(total(scores))
print(average(scores))
