# /usr/bin/env python

var1 = list(range(10))
var2 = list(range(10))
res = []


def intersection(arg1, arg2):
    res = []
    for each in arg1:
        if each in arg2:
            res.append(each)

    return res


print(intersection(var1, var2))
print(res)
