scores = [80,100,70,90,40]

def total(n):
    hap=0
    for i in range(len(n)):
        hap+=n[i]
    return hap

def average(n):
    return total(n)/len(n)

def test_total():
    assert total(scores) == 380

def test_average():
    assert average(scores) == 76