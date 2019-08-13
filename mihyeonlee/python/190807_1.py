scores = [80, 100, 70, 90, 40]
def total(list_name):
    accumulator = 0
    for i in range(0, len(list_name)):
        accumulator += list[i]
    return accumulator
print(total(scores))
##################################
scores = [80, 100, 70, 90, 40]
def total(list):
    accumulator = 0
    for i in range(0, len(list)):
        accumulator += list[i]
    return accumulator
print(total(scores))