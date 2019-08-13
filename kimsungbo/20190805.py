'''
when a list called scores is given as following:
scores = [80, 100, 70, 90, 40]

1. create total function
2. create average function
3. check if the functions are correct
'''


scores = [80, 100, 70, 90, 40]


# calculate sum of the list
def total(list):
    return sum(list)


# calculate average of the list
def average(list):
    return sum(list) / len(list)


print("total", total(scores))
print("average", average(scores))

# check if the functions are correct
assert total([]) == 0
assert total([1, 2]) == 1 + 2
assert total([1, 2, 5]) == 1 + 2 + 5

assert average([1, 2]) == (1 + 2) / 2
assert average([1, 2, 5]) == (1 + 2 + 5) / 3
