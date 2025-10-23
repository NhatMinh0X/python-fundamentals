#!/usr/bin/env python3
# demo_args_kwargs.py
def f(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args (positional extra):", args)
    print("kwargs (named extra):", kwargs)

if __name__ == "__main__":
    # gọi với nhiều positional và keyword
    f(1, 2, 3, 4, x=10, y=20)