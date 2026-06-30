import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import calculate_total


def test_calculate_total():
    assert calculate_total(20, 3) == 60