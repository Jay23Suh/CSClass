"""
    Test cases for Search Performance lab

    This starter includes a set of basic sanity checks for the
    assigned functions in part 1 and part 2 of this lab.  The
    provided tests cases check returned types and values for
    the simplest cases.

    Extend these test cases (especially linear_search_tester
    and binary_search_tester) to better exercise the interesting
    situations for those searches.  You will be graded on the
    completeness of the added test cases.
"""
from search_performance import *


def list_builder_tester():
    """
    Run a series of tests for the list builder
    :return (boolean): were all tests successful
    """
    # value we expect to see
    list_size = 64
    min_value = 1
    max_value = 2 * list_size

    result = list_of_integers(list_size)

    # confirm the size of the list
    assert (len(result) == list_size)

    # validate the contents
    for value in result:
        # check the type
        assert (type(value) == int)

        # check vs max/minimum value
        assert (value >= min_value)
        assert (value <= max_value)

    return True


def linear_search_tester():
    """
    Run a series of tests for linear_search
    :return (boolean): were all tests successful
    """

    unsorted_list = [8, 2, 6, 4]

    # find a number in the middle of the list
    result = linear_search(unsorted_list, 2)
    assert (type(result == int))
    assert (result == 1)

    # find a number that is not in the list
    result = linear_search(unsorted_list, 5)
    assert (type(result == int))
    assert (result == -1)

    # check a list with no elements
    unsorted_list_one = []

    result = linear_search(unsorted_list_one, 3)
    assert (type(result) == int)
    assert (result == -1)

    # unsorted list with odd number of elements
    unsorted_list_two = [33, 31, 27, 7, 11, 13, 17, 21, 23]

    # find a number that is first in the list
    result = linear_search(unsorted_list_two, 33)
    assert (type(result) == int)
    assert (result == 0)

    # find a number that is last in the list
    result = linear_search(unsorted_list_two, 23)
    assert (type(result) == int)
    assert (result == 8)

    # find a number somewhere in the middle of the list
    result = linear_search(unsorted_list_two, 11)
    assert (type(result) == int)
    assert (result == 4)

    # find a number not in the list
    result = linear_search(unsorted_list_two, 24)
    assert (type(result) == int)
    assert (result == -1)

    # check list with one element
    unsorted_list_three = [3]

    result = linear_search(unsorted_list_three, 3)
    assert (type(result) == int)
    assert (result == 0)

    return True


def binary_search_tester():
    """
    Run a series of tests for binary_search
    :return (boolean): were all tests successful
    """
    sorted_list = [2, 4, 6, 8]

    # find a number in the middle of the list
    result = binary_search(sorted_list, 4)
    assert (type(result == int))
    assert (result == 1)

    # find a number that is not in the list
    result = binary_search(sorted_list, 5)
    assert (type(result == int))
    assert (result == -1)

    # check an empty list
    sorted_list_one = []

    result = binary_search(sorted_list_one, 10)
    assert (type(result == int))
    assert (result == -1)

    # sorted list that has odd number of elements
    sorted_list_two = [1, 1, 2, 3, 5, 8, 13, 21, 34]

    # find a number in the middle of the list
    result = binary_search(sorted_list_two, 5)
    assert (type(result == int))
    assert (result == 4)

    # find a number in the first half and in the first quarter of the list (first number)
    result = binary_search(sorted_list_two, 1)
    assert (type(result == int))
    assert (result == 0)

    # find a number in the middle of the first half of the list
    result = binary_search(sorted_list_two, 2)
    assert (type(result == int))
    assert (result == 2)

    # find a number in the first half and in the second quarter of the list
    result = binary_search(sorted_list_two, 3)
    assert (type(result == int))
    assert (result == 3)

    # find a number in the second half and in the third quarter
    result = binary_search(sorted_list_two, 8)
    assert (type(result == int))
    assert (result == 5)

    # find a number in the middle of the second half
    result = binary_search(sorted_list_two, 13)
    assert (type(result == int))
    assert (result == 6)

    # find a number in the second half and in the last quarter (last number)
    result = binary_search(sorted_list_two, 34)
    assert (type(result == int))
    assert (result == 8)

    # check a list with a single value
    sorted_list_three = [2, 5]

    # first value
    result = binary_search(sorted_list_three, 2)
    assert (type(result == int))
    assert (result == 0)

    # last value
    result = binary_search(sorted_list_three, 5)
    assert (type(result == int))
    assert (result == 1)

    return True


def sorted_search_tester():
    """
    Run a series of tests for sorted searches
    :return (boolean): were all tests successful
    """
    result = sorted_comparison(2, 8)

    # confirm the number of tupples
    assert (len(result) == 3)

    # confirm count and types of values in each tupple
    size = 2
    for index in range(3):
        (count, linear, binary) = result[index]
        assert (type(count) == int)
        assert (type(linear) == float)
        assert (type(binary) == float)
        assert (count == size)
        size *= 2

    return True


def unsorted_search_tester():
    """
    Run a series of tests for sorted searches
    :return (boolean): were all tests successful
    """
    result = unsorted_comparison(2, 8)

    # confirm the number of tupples
    assert (len(result) == 3)

    # confirm count and types of values in each tupple
    size = 2
    for index in range(3):
        (count, linear, binary) = result[index]
        assert (type(count) == int)
        assert (type(linear) == float)
        assert (type(binary) == float)
        assert (count == size)
        size *= 2

    return True


def main():
    """
    exercise the assigned methods
    """
    print("testing linear search ... " +
          "PASS" if linear_search_tester() else "FAIL")

    print("")
    print("testing binary search ... " +
          "PASS" if binary_search_tester() else "FAIL")

    print("")
    print("testing list of integers ... " +
          "PASS" if list_builder_tester() else "FAIL")

    """
    un-coment for part 2
    print("")
    print("testing sorted_comparison ... " +
          "PASS" if sorted_search_tester() else "FAIL")

    print("")
    print("testing unsorted_comparison ... " +
          "PASS" if unsorted_search_tester() else "FAIL")
    """


if __name__ == "__main__":
    main()
