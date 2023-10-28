import functools


# TODO ref https://stackoverflow.com/a/38755760
def pipeline(*funcs):
    return lambda x: functools.reduce(lambda f, g: g(f), list(funcs), x)

__all__ = [
    pipeline
]
