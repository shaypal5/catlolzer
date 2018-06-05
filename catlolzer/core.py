"""Core functionalities for catlolzer."""

import numpy as np


class CatLolzer(object):
    """An advanced cat lolzing engine.

    Parameters
    ----------
    alpha : int
        The main cat lolzing factor.
    """

    def __init__(self, alpha):
        self.alpha = alpha

    def lolize(self, cat):
        """Apply this catlolzing engine to the given cat.

        Parameters
        ----------
        cat : Cat
            The input cat to lolz.

        Returns
        -------
        lolcat
            The lolized cat.
        """
        return np.zeros(self.alpha)
