import pytest

def test_inc(x):
    return x + 2

def test_answer():
    assert test_inc(3) == 5 , "Assertion Failed"