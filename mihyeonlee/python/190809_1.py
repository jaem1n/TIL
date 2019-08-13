print(1 + 2)
assert 1 + 1 == 2
# assert 1 + 2 == 2

def double(n):
    # todo 작업 해야 함
    return n * 2


assert double(2) == 4
assert double(1) == 2
assert double(1234) == 2468

print(double(2))
print(double(1))
print(double(1234))
print(double(2468))


def test_simple():
    assert 1 + 1 == 2
