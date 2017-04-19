import math
from functools import reduce


class Function:
    """
    Generic function representation
    """

    def __init__(self, start, end):
        """
        Initialize a new function object
        :param start: First 'relevant' value in the function's domain
        :param end: Last 'relevant' value in the function's domain
        """
        self.start = start
        self.end = end

    def __call__(self, x):
        raise NotImplementedError()

    def points(self, step=0.1):
        """
        Generator of tuples (x, f(x)) in the interval [self.start, self.end]
        :param step: Distance between points in the discretized function domain
        """
        x = self.start
        while x < self.end:
            yield x, self(x)
            x += step


class Compose(Function):
    """
    Represents the composition of several functions
    """

    def __init__(self, aggr):
        """
        Initialize a new composed function
        :param aggr: List of tuples (trunc, func) where trunc is an upper limit to func's image
        """

        self.aggr = aggr

        # Store smallest start in member functions as the own's start
        start = reduce(
            lambda x, y: x if x[1].start < y[1].start else y,
            aggr,
            aggr[0]
        )[1].start

        # Store biggest end in member functions as the own's end
        end = reduce(
            lambda x, y: x if x[1].end > y[1].end else y,
            aggr,
            aggr[0]
        )[1].end

        super().__init__(start, end)

    def __call__(self, x):
        # Check produced image of each member function and keep the greatest
        y = 0
        for trunc, func in self.aggr:
            yi = min(trunc, func(x))  # Trunc function if necessary
            y = max(y, yi)
        return y


class Trapezoid(Function):
    def __init__(self, a, b, c=None, d=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        super().__init__(a, d if d else c if c else b)

    def __call__(self, x):
        if self.a is not None:
            if x <= self.a:
                return 0  # (inf, a]

            if self.a < x < self.b:
                return (x - self.a) / (self.b - self.a)  # (a, b)

        if self.c is None or self.b <= x <= self.c:
            return 1  # [b, inf) or [b, c]

        if self.d is None or x < self.d:
            # Descent (b->c if triangle, c->d if trapezoid)
            c, d = (self.c, self.d) if self.d is not None else (self.b, self.c)
            return (x - d) / (c - d)  # (b, c) or (c, d)

        return 0  # [c, inf) or [d, inf)


class Triangle(Trapezoid):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)


class Sigmoid(Function):
    def __init__(self, k, x0):
        self.k = k  # width
        self.x0 = x0  # center
        super().__init__(start=-abs(6 / k), end=abs(6 / k))  # thanks Wikipedia

    def __call__(self, x):
        return 1 / (1 + math.e ** (-self.k * (x - self.x0)))


class Gaussian(Function):
    def __init__(self, b, c):
        self.b = b  # center
        self.c = c  # width
        super().__init__(start=-abs(6 * c), end=abs(6 * c))

    def __call__(self, x):
        return math.e ** -(((x - self.b) ** 2) / (2 * self.c ** 2))
