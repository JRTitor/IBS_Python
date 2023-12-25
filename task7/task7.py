def chain_sum(num):
    result = num

    def wrapper(num2=None):
        nonlocal result
        if num2 is None:
            return result
        result += num2
        return wrapper

    return wrapper


