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


def sort(data, by_key=True, key=lambda x: x, reverse=False):
    if isinstance(data, dict):
        return dict(sorted(data.items(), key=lambda x: key(x[not by_key]), reverse=reverse))
    return sorted(data, key=key, reverse=reverse)


def first(func, array):
    return next(filter(func, array), None)
