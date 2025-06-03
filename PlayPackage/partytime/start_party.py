# partytime/start_party.py

from PlayPackage import ConfettiCannon


def start_party():
    """
    Starts a party by firing a confetti cannon.
    """
    print("Party time! Let's get the confetti flying!")
    cannon = ConfettiCannon(color="rainbow")
    cannon.fire()
    print("The party has started with a bang of confetti!")
