from test import select_high_scores


def test_select_high_scores():
    assert select_high_scores([], 50) == []
    assert select_high_scores([60], 50) == [60]
    assert select_high_scores([60, 40], 50) == [60]
    assert select_high_scores([60, 40, 50], 50) == [60, 50]
    assert select_high_scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 50) == [50, 60, 70, 80, 90, 100]