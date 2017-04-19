def centroid(func, step=0.1):
    """
    Determine the center of gravity (centroid) of a function's curve
    :param func: Function object
    :param step: Distance between domain's values
    :return: Numeric value representing the domain's value which approximately corresponds to the centroid
    """
    points = func.points(step)
    num, den = 0, 0

    for x, y in points:
        num += x * y
        den += y

    return num / den


def bisecter(func, step=0.1):
    """
    Determine the center of area (splits the curve in two pices with the same area) (bisecter) of a function
    :param func: Function object
    :param step: Distance between domain's values
    :return: Numeric value representing the domain's value which approximately corresponds to the bisecter
    """
    points = list(func.points(step))
    area = sum(map(lambda p: p[1], points))

    current = 0.
    for x, y in points:
        current += y
        if current >= area / 2:
            return x


def mean_max(func, step=0.1):
    """
    Determine the point which corresponds with the mean of the function's maximums
    :param func: Function object
    :param step: Distance between domain's values
    :return: Numeric value representing the domain's value which approximately corresponds to the mean of maximums
    """
    points = func.points(step)
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
