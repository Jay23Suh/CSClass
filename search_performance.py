"""
    CS051P Lab Assignments: Search Performance

    Author: Jayhyun Suh

    Date:   7 November 2022

    The goal of this assignment is to implement a few basic search
    algorithms and measure their performance.  As such, it is also
    an introduction to algorithmic complexity.
"""
import random
import time
import csv


def list_of_integers(size):
    """
    creates a new list by appending a random number between 1 and 2 * size in a for loop with a range of size
    size: (int) the number of elements in the created list
    """

    # new list
    create_list = []

    # for loop that appends a random integer between 2 * size, size number of times
    for _ in range(size):
        create_list.append(random.randint(1, 2 * size))

    return create_list


def linear_search(alist, value):
    """
    Goes through each element in alist and searches for a match of value. If value is not in alist, return -1
    alist: (list) a list of values
    value: (int) a number that we are looking for in the list
    :return: (int) either index of value or -1
    """

    # for the length of the list, if the value is present, return the first index number
    for i in range(len(alist)):
        if alist[i] == value:
            return i

    # if value is not in the list, return -1
    return -1


def binary_search_helper(alist, value, start, end):
    """
    If the value is not in the list, return -1. If value is in the list, return the index number of the value. It
    recursively searches for a middle value between an interval and checks to see if the value is greater, less, or
    equal to that middle number
    alist: (list) a list of integers
    value: (int) the number we are looking for in the list
    start: (int) the index of where we start the search for the value in alist
    end: (int) the index of where we end the search for the value in alist
    :return: either index of value or -1
    """

    # special cases where alist is either empty or the first value is the value we are looking for
    if alist == []:
        return -1

    if alist[0] == value:
        return 0

    # middle changes through each call of the function that is
    middle = start + int((end - start) / 2)

    # base case: the length is too short or value is not in the list
    if end - start < 2:
        return -1

    # if the middle value of an interval is the value, return middle
    elif alist[middle] == value:
        return middle

    # recursive case: if the index of the middle number is greater than the value, calls the function between the
    # start and new middle value as the end point
    elif alist[middle] > value:
        return binary_search_helper(alist, value, start, middle)

    # recursive case: if the index of middle number is less, calls the function for a search in the latter half of
    # the interval
    elif alist[middle] < value:
        return binary_search_helper(alist, value, middle, end)


def binary_search(alist, value):
    """
    Uses helper function binary_search
    alist: (list) a list of integers
    value: (int) a value we look for
    :return: (int) return value from helper function
    """
    return binary_search_helper(alist, value, 0, len(alist))


def main_part1():
    """
    creates a list of size 5, tests two cases of linear_search and two cases of binary_search
    """
    print(sorted_comparison(2, 500))
    alist = list_of_integers(5)
    linear_search(alist, 3)
    linear_search(alist, 2)
    alist.sort()
    binary_search(alist, 4)
    binary_search(alist, 1)


#
# the following functions are to be implemnted in part 2
#


def sorted_comparison(min_size, max_size):
    """
    From a list of integers made from list_of_integers, creates a series of list with each list of information on
    size of list, time to complete linear_search and binary_search The sorting of list is not included in this time.
    min_size: (int) starting length of random integer list
    max_size: (int) maximum length of the list
    :return: list containing all the lists with length of random integer list and time to complete two sorting functions
    """

    # empty list
    return_list = []

    # while max_size is not reached, run prompts inside
    while min_size <= max_size:
        # empty list that is reset each increase in size of list
        sort_descriptive = []

        # creates a random list and sorts it
        random_list = list_of_integers(min_size)
        random_list.sort()

        # measure time for a value not in the list for linear_search
        start = time.time()
        linear_search(random_list, 0)
        end = time.time()
        elapsed_time_in_seconds1 = end - start

        # measure tme for a value not in an already sorted list for binary_search
        start = time.time()
        binary_search(random_list, 0)
        end = time.time()
        elapsed_time_in_seconds2 = end - start

        # append information to a list called sort_descriptive
        sort_descriptive.append(len(random_list))
        sort_descriptive.append(elapsed_time_in_seconds1)
        sort_descriptive.append(elapsed_time_in_seconds2)

        # append sort_descriptive to a bigger list
        return_list.append(sort_descriptive)

        # a bigger size list next time it is called
        min_size = min_size * 2

    return return_list


def unsorted_comparison(min_size, max_size):
    """
    From a list of integers made from list_of_integers, creates a series of list until it reaches maximum size with
    each list of information on size of list, time to complete linear_search and binary_search The time sorting the
    list is included for the binary_search.
    min_size: (int) starting length of random integer list
    max_size: (int) maximum length of the list
    :return: list containing all the lists with length of random integer list and time to complete two sorting functions
    """

    # empty list
    unsorted_return = []

    # create list as long as size of the list is less than max_size
    while min_size <= max_size:

        # empty list that is reset each increase in size of list
        unsort_descriptive = []
        unsorted_random = list_of_integers(min_size)

        # measure time for a value not in the list for linear_search
        start = time.time()
        linear_search(unsorted_random, 0)
        end = time.time()
        elapsed_time_in_seconds1 = end - start

        # measure time to search for a value not in a list that needs to be sorted
        start = time.time()
        unsorted_random.sort()
        binary_search(unsorted_random, 0)
        end = time.time()
        elapsed_time_in_seconds2 = end - start

        # append information to a list called unsort_descriptive
        unsort_descriptive.append(len(unsorted_random))
        unsort_descriptive.append(elapsed_time_in_seconds1)
        unsort_descriptive.append(elapsed_time_in_seconds2)

        # append sort_descriptive to a bigger list
        unsorted_return.append(unsort_descriptive)

        # a bigger size list next time it is called
        min_size = min_size * 2
    return unsorted_return


def main():
    """
    Calls sorted_comparison and unsorted_comparison with parameters 2 and 1048576 as minimum and maximum list size.
    Write data for sorted_comparison line by line to sorted.csv and data for unsorted_comparison to unsorted.csv
    """

    # open files and prepare for writing
    file_sort = open("sorted.csv", "w")
    file_unsort = open("unsorted.csv", "w")
    writer = csv.writer(file_sort)
    writer2 = csv.writer(file_unsort)

    # calls comparison functions into s_list and us_list to store the return lists there
    s_list = sorted_comparison(2, 1048576)
    us_list = unsorted_comparison(2, 1048576)

    # for each list in the big list, write the list into a line for sorted.csv
    for one_line in s_list:
        writer.writerow(one_line)

    # for each list in the total list, wrote the list into a line for unsorted.csv
    for one_line in us_list:
        writer2.writerow(one_line)

    file_sort.close()
    file_unsort.close()


if __name__ == "__main__":
    # main()  # un-comment for part 2
    main_part1()  # comment out for part 2
