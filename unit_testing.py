__author__ = 'drake'


def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

test_answer()

#using py.test get an assertion error, but changing the testing parameters to equal "4" returns a pass