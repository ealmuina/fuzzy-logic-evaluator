def centroid(func_aggr, step=0.1):
    points = func_aggr.points(step)
    num, den = 0, 0

    for x, y in points:
        num += x * y
        den += y

    return num / den


def bisecter(func_aggr, step=0.1):
    points = list(func_aggr.points(step))
    area = sum(map(lambda p: p[1], points))

    current = 0.
    for x, y in points:
        current += y
        if current >= area / 2:
            return x


def mean_max(func_aggr, step=0.1):
    points = func_aggr.points(step)
    maximums = []
    k = 0

    for x, y in points:
        if abs(y - k) < 1e-6:  # y == k
            maximums.append(x)
        elif y > k:
            k = y
            maximums.clear()
            maximums.append(x)

    return sum(maximums) / len(maximums)
