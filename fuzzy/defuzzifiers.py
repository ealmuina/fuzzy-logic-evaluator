def centroid(func_aggr, start, stop, step=0.1):
    di = start
    num = 0
    den = 0

    while di <= stop:
        miu = func_aggr(di)
        num += di * miu
        den += miu
        di += step

    return num / den


def bisecter():
    pass


def mean_max():
    pass


def get_defuzzy(name):
    if name == 'centroid':
        return centroid
    elif name == 'bisecter':
        return bisecter
    elif name == 'mean of max':
        return mean_max
