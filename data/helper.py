from collections import defaultdict


def split_dict(dictionary):
    return dictionary.keys(), dictionary.values()


def index(array):
    return range(len(array))


def count(func, array):
    res = defaultdict(int)
    for entry in array:
        group = func(entry)
        res[group] += 1
    return res


def count_list(func, array):
    res = defaultdict(int)
    for entry in array:
        group = func(entry)
        for item in group:
            res[item] += 1
    return res


def sort(data, descending=False, value_based=True, key=None):
    if isinstance(data, dict):
        return dict(sorted(data.items(), key=key if key else lambda x: x[value_based], reverse=descending))
    return sorted(data, key=key, reverse=descending)


def first(func, array):
    return next(filter(func, array), None)
