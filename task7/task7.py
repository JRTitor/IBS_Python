def chain_sum(num: int) -> Callable[[int], int]:
    """
    Returns a function that when called with an argument adds it to the original number.
    The returned function continues to remember the sum of all the arguments passed to it.

    Args:
        num (int): The initial number to start with.

    Returns:
        Callable[[int], int]: A function that takes an argument and returns the sum of the original number and the argument.
    """

    result = num

    def wrapper(num2: int = None) -> int:
        """
        Adds the argument to the original number and returns the sum.

        Args:
            num2 (int, optional): The number to be added to the original number. Defaults to None.

        Returns:
            int: The sum of the original number and the argument.
        """
        nonlocal result
        if num2 is None:
            return result
        result += num2
        return wrapper

    return wrapper


