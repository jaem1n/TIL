class_scores = [{'국어': 80, '영어': 100, '수학': 50},
                {'국어': 90, '영어': 70, '수학': 40}]


def class_total(list, subject):
    subject_total = 0
    for i in range(len(list)):
        subject_total += list[i][subject]
    return subject_total


def class_total_all(list):
    total = 0
    for subject in list[0].keys():
        total += class_total(list, subject)
    return total


print(class_total(class_scores, '국어'))
print(class_total(class_scores, '영어'))
print(class_total(class_scores, '수학'))
print(class_total_all(class_scores))
