import functools
import time


__all__ = ['logging', 'time_it', 'enforce_types', 'debug_func']


def logging(func):
    """ Logs when a function starts and ends by printing to the console

    Examples
    --------
    >>> @logging
    >>> def say_hello(name):
    >>>     print(f"Hello, {name}!")
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}.")
        return result
    return wrapper


def time_it(func):
    """ Measures the time a function takes to execute

    Examples
    --------
    >>> @time_it
    >>> def some_function():
    >>>     time.sleep(2)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper


def enforce_types(*arg_types):
    """Enforces argument types for a function

    Examples
    --------
    >>> @enforce_types(str, int)
    >>> def greet(name, age):
    >>>     print(f"Hello, {name}. You are {age} years old.")
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for (a, t) in zip(args, arg_types):
                if not isinstance(a, t):
                    raise TypeError(f"Expected type {t}, but received {type(a)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def debug_func(func):
    """Prints arguments and return value of the function

    Examples
    --------
    >>> @debug_func
    >>> def example_function(a, b=5):
    >>>     return a + b
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ', '.join(repr(arg) for arg in args)
        kwarg_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        call_str = f"{func.__name__}({arg_str}, {kwarg_str})"
        print(f"Calling: {call_str}")
        result = func(*args, **kwargs)
        print(f"{call_str} returned {result!r}")
        return result
    return wrapper
