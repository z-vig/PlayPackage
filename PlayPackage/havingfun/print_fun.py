from .calculate_fun import calculate_fun


def print_fun(fun_prior: float = 5.0) -> float:
    """
    Prints a fun message to the console.
    This function is part of the PlayPackage's havingfun module.

    Parameters
    ----------
    fun_prior : float, optional
        A prior fun value that influences the calculation, by default 5.0
    Returns
    -------
    float
        The calculated fun value based on the prior fun value.
    """
    print("Let's have some fun with PlayPackage! 🎉")
    print("Remember, the more you play, the more you learn!")
    print("Keep exploring and enjoy your coding journey! 🚀")
    return calculate_fun(fun_prior)
