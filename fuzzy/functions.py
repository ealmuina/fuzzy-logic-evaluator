class Trapezoid:
    def __init__(self, a, b, c=None, d=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

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


class Polynomial:
    pass


class Compose:
    def __init__(self, aggr):
        self.aggr = aggr

    def __call__(self, x):
        y = 0
        for func, trunc in self.aggr:
            yi = min(trunc, func(x))
            y = max(y, yi)
        return y
