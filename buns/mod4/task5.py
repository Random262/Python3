import collections


def countfreq(name):
    res = {}
    text = open(name, 'r', encoding='utf-8')
    for i in text:
        for j in i:
            if j.isalpha():
                if j not in res:
                    res[j] = 0
                res[j] += 1
    text.close()
    return res


def sortdict(dict):
    val = sorted(dict.values())
    sdict = collections.OrderedDict()
    for i in val:
        for j in dict.keys():
            if dict[j] == i:
                sdict[j] = dict[j]
    return sdict


a = input()
ans = countfreq(a)
ans = sortdict(ans)
for i, j in ans.items():
    print(i, ':', j)
