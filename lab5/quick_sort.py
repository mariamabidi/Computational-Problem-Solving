__author__ = 'MC'

"""
CSCI-603 Lab 5: Quick Sort

A program to sort a list using quick sort algorithm.

Author: Maria Cepeda
"""


def partition(laser_list: list, pivot: int) -> tuple[list, list, list]:
    """
    A function to partition the list into three different lists.
    :param laser_list:
    :param pivot:
    :return:
    """
    less, equal, greater = [], [], []
    for laser in laser_list:
        if laser.total_sum == pivot:
            equal.append(laser)
        elif laser.total_sum > pivot:
            greater.append(laser)
        else:
            less.append(laser)

    return less, equal, greater


def quick_sort_list(laser_list: list):
    """
    The function which handles quick sort.
    :param laser_list: A variable to store the list
    :return:
    """
    if len(laser_list) == 0:
        return []
    else:
        pivot = laser_list[0].total_sum
        less, equal, greater = partition(laser_list, pivot)
        return quick_sort_list(greater) + equal + quick_sort_list(less)
