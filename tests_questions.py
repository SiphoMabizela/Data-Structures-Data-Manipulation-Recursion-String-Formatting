import pytest

from question1 import count_occurrences
from question2 import filter_even_numbers
from question3 import sum_to_n
from question4 import format_user
from question5 import merge_and_sort


# -------------------------
# QUESTION 1: Data Structures
# -------------------------

def test_count_occurrences_basic():
    assert count_occurrences([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}

def test_count_occurrences_strings():
    assert count_occurrences(["a", "b", "a"]) == {"a": 2, "b": 1}

def test_count_occurrences_empty():
    assert count_occurrences([]) == {}


# -------------------------
# QUESTION 2: Data Manipulation
# -------------------------

def test_filter_even_numbers_mixed():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_filter_even_numbers_all_odd():
    assert filter_even_numbers([1, 3, 5]) == []

def test_filter_even_numbers_empty():
    assert filter_even_numbers([]) == []


# -------------------------
# QUESTION 3: Recursion
# -------------------------

def test_sum_to_n_positive():
    assert sum_to_n(5) == 15

def test_sum_to_n_one():
    assert sum_to_n(1) == 1

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0


# -------------------------
# QUESTION 4: String Formatting
# -------------------------

def test_format_user_basic():
    assert format_user("Sipho", 25) == "Name: Sipho | Age: 25"

def test_format_user_age_zero():
    assert format_user("Alex", 0) == "Name: Alex | Age: 0"

def test_format_user_spacing():
    assert format_user("John", 30) == "Name: John | Age: 30"


# -------------------------
# QUESTION 5: Data Structures + Manipulation
# -------------------------

def test_merge_and_sort_basic():
    assert merge_and_sort([3, 1], [2, 4]) == [1, 2, 3, 4]

def test_merge_and_sort_duplicates():
    assert merge_and_sort([1, 2], [2, 3]) == [1, 2, 2, 3]

def test_merge_and_sort_empty():
    assert merge_and_sort([], [5, 1]) == [1, 5]
