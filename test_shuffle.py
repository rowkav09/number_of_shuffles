from shuffle import num_shuffle
import pytest

def test_no_repeats():
    assert num_shuffle('DEAN') == 24

def test_one_repeat():
    assert num_shuffle('ROSALIA') == 2520

def test_multiple_repeats():
    assert num_shuffle('HERBERT') == 1260
