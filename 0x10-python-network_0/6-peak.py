#!/usr/bin/python3
"""
Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity
(hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of
your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
"""


def find_peak(list_of_integers):
    uniq_list = list(set(list_of_integers))
    n = len(uniq_list)

    if not uniq_list:
        return None
    if n == 1:
        return uniq_list[0]
    maximum = uniq_list[0]
    for i in uniq_list:
        if i > maximum:
            maximum = i
    return maximum
