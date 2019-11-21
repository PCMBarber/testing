import pytest
from excercises import multiply_list

def test_negatives():
    assert multiply_list.product([-2,-1,-2])==-4

def test_zero():
    assert multiply_list.product([0,0,0])==0

def test_big_list():
    assert multiply_list.product([2,2,2,2,2,2,2])==128

def test_float():
    assert multiply_list.product([2.5,3,2.7])==20.25
