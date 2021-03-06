import numpy as np
from copy import deepcopy


class AlgoDecider:
    threshold = 80
    sum_threshold = 1000
    max_size = 9

    def decide(self, reds):
        reds = self._extend_points(reds)
        print(reds)
        columns = reds.sum(axis=0)
        max_column = np.argmax(columns)

        if np.amax(reds) < self.threshold:
            return 1
        else:
            if np.amax(columns) > self.sum_threshold:
                return 0
            elif max_column < 3:
                return 2
            elif max_column > 7:
                return 3
            else:
                return 4

    def _extend_points(self, reds):
        extended = deepcopy(reds)
        for index, element in np.ndenumerate(extended):
            i = index[0]
            j = index[1]
            extended[i, j] = (2 * element
                              + reds[self._bound(i - 1), j]
                              + reds[self._bound(i + 1), j]) // 4

        return extended

    def _bound(self, i):
        if i < 0:
            return 0
        elif i > self.max_size:
            return self.max_size
        else:
            return i
