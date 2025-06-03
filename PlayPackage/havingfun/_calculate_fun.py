import numpy as np


def calculate_fun(fun_prior: float) -> float:
    """
    Calculates a fun value based on a simple formula.
    This function is part of the PlayPackage's havingfun module.

    Parameters
    ----------
    fun_prior : float
        A prior fun value that influences the calculation.

    Returns
    -------
    float
        The calculated fun value based on the prior fun value.
    """
    fun_coef = np.random.uniform(0.5, 1.5)  # Random coefficient for fun
    fun_value = fun_coef * 42 + np.sqrt(fun_prior)  # A fun constant
    print(f"The calculated fun value is: {fun_value}")
    if fun_value > 50:
        print("Wow! That's a lot of fun! 🎉")
    elif fun_value < 30:
        print("Hmm, not so much fun. Let's try harder! 😅")
    else:
        print("That's a decent amount of fun! Keep it up! 😊")
    return fun_value
