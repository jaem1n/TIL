from scores import total_class
import pandas as pd


def main():
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
    total = {'name', '<Total>'}
    for subject in ['국어', '영어', '수학']:
        total[subject] = total_class(class_scores, subject)

    table = pd.DataFrame(class_scores + [total],
                         columns=['Name', 'Korean', 'English', 'Math'])
    print(table)
