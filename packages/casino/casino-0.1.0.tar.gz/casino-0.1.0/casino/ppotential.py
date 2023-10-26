import numpy as np
import numba as nb

ppotential_spec = [
    ('neu', nb.int64),
    ('ned', nb.int64),
]


@nb.experimental.jitclass(ppotential_spec)
class PPotential:

    def __init__(self, neu, ned):
        """
        :param neu: number of up electrons
        :param ned: number of down electrons
        """
        self.neu = neu
        self.ned = ned

    def value(self, n_vectors: np.ndarray) -> float:
        """Value φ(r)
        :param n_vectors: electron-nuclei vectors shape = (natom, nelec, 3)
        """
        return 0
