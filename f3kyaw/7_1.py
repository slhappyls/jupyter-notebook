class IntTuple(tuple):
    def __new__(cls, iterable):
        # 过滤iterable
        f_it = (e for e in iterable if isinstance(e, int) and e > 0)
        return super().__new__(cls, f_it)












int_t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(int_t)








