class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]


def class_total(list_dictionary, x):
    total = 0
    for i in range(len(list_dictionary)):
        total += list_dictionary[i][x]
    return total

class_total(class_scores, '영어')

def test_class_total():
    assert class_total(class_scores, '국어') == 170

