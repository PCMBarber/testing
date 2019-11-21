import pytest
from excercises import anti_vowel

def test_vowel_remove():
    assert anti_vowel.anti_vowel("supercalifragilisticexpialidocious")=="sprclfrglstcxpldcs"

def test_no_vowel():
    assert anti_vowel.anti_vowel("Rythm")=="Rythm"

def test_all_vowel():
    assert anti_vowel.anti_vowel("aoiueiaoeuo")==""
