import numpy as np


class ConfettiCannon:
    """
    A class representing a confetti cannon that can be fired to release
    confetti.
    """
    def __init__(self, color: str):
        """
        Initializes the ConfettiCannon with a specific color.

        Parameters
        ----------
        color : str
            The color of the confetti to be released by the cannon.

        Attributes
        ----------
        color : str
            The color of the confetti.
        released_confetti : int
            The number of confetti pieces released by the cannon.
        """
        self.color = color
        self.released_confetti = 0

    def fire(self):
        """
        Fires the confetti cannon, releasing confetti of the specified color.
        """
        n_pieces = np.random.randint(50, 200)
        for _ in range(n_pieces):
            self._release_confetti()
        print(f"Firing confetti cannon with {self.color} confetti!")

    def _release_confetti(self, print_message: bool = True):
        """
        Simulates the release of a single piece of confetti.
        This method can be extended to include more complex behavior
        such as physics simulation or visual effects.
        """
        # Here we would normally have code to visually represent the confetti
        # For now, we just simulate it with a print statement
        self.released_confetti += 1
        if print_message:
            print(f"Released a piece of {self.color} confetti!")
