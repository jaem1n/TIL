class_scores = [
    {
        'K': 80,
        'E': 100,
        'M': 50
    },
    {
        'K': 90,
        'E': 70,
        'M': 40
    }
]


"""
!~Problem~
Suddenly, Korean is not available in Python, so the names of the subjects are abbreviated.
K = Korean, E = English, M = Math

class_total(class_scores, 'k') == 170
class_total_all(class_scores) == 430
"""

def class_total(scores, subject):
   total_sum = 0
   for dic in scores:
       total_sum += dic[subject]
   return total_sum

def test_class_total():
   assert class_total(class_scores, 'K') == 80 + 90
   assert class_total(class_scores, 'E') == 100 + 70
   assert class_total(class_scores, 'M') == 50 + 40

def class_total_all(scores):
   total_all_sum = 0
   for dic in scores:
       for num in dic.values():
           total_all_sum += num
   return total_all_sum

def test_class_total_all():
   assert class_total_all(class_scores) == 80 + 100 + 50 + 90 + 70 + 40


