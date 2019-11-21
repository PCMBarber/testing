import pytest
from excercises import count

def test_count_zeros():
    assert count.count([0,0,0],0)==3

def test_count_string():
    assert count.count(["a","a","a"],"a")==3

def test_count_negatives():
    assert count.count([-2,-2,2],-2)==2

def test_count_capitals():
    assert count.count(["B","B","b"],"B")==2

