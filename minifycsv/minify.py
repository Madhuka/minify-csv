#!/usr/bin/python
# -*- coding: utf-8 -*-


def spilter(str):
    """Making array of values in csv"""

    array = str.split(',')
    return array


def grouping(csv_values, val_count):
    """Making two array with value id and count"""

    count = 1
    count_array = []
    csv_value_ids = []

    # print csv_values

    for (index, page) in enumerate(csv_values):

        if index < len(csv_values) - 1:
            next = csv_values[index + 1]
        if page == next:
            count += 1
        else:
            csv_value_ids.append(page)
            count_array.append(count)
            count = 1

        if index == len(csv_values) - 1:
            csv_value_ids.append(page)
            count_array.append(count - 1)

    return make_string_regex(csv_value_ids, count_array)


def make_stringline_regex(value_id, val_count):
    """making regex represtation"""

    out_str = ''
    if val_count == 1:
        out_str = value_id
    else:
        out_str = str(value_id) + '[1:' + str(val_count) + ']'
    return out_str


def make_string_regex(list_s, list_count):
    """makgin string of regex by using two arrays"""

    out_str = ''
    for (my_index, vlaue_Id) in enumerate(list_s):
        count_list = list_count[my_index]
        out_str = out_str + make_stringline_regex(vlaue_Id, count_list) \
            + ', '   
    out_str = out_str[:-2]
    return out_str