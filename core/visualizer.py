import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import core.constants as const


class Visualizer(object):

    def __init__(self):
        super(Visualizer, self).__init__()

        self._jnt_indices = const.DUMMY_INDICES.copy()
        self.fig = None

    def _get_default_parents(self):
        joint_names = list(self._jnt_indices.keys())
        parents = []

        for name in joint_names:
            if const.DEFAULT_PARENTS[name] is not None:
                parents.append(joint_names.index(const.DEFAULT_PARENTS[name]))
            else:
                parents.append(-1)

        return parents

    def open_figure(self, figsize=(10, 10)):
        self.fig = plt.figure(figsize=figsize)

    def show_figure(self):
        plt.show()

    def plot_2d(self, joints=None, parents=None, names=None,
                left=None, right=None, subplot=None):

        if subplot is None:
            self.open_figure()
            subplot = self.fig.add_subplot(111)
            subplot.set_xlim((-1, 1))
            subplot.set_ylim((-1, 1))

        if joints is None:
            joints = np.vstack(self._jnt_indices.values())
        else:
            joints = [self._jnt_indices[names[i]] for i in range(len(joints))]
            joints = np.vstack(joints)

        if parents is None:
            parents = self._get_default_parents()

        if names is None:
            names = list(self._jnt_indices)

        labels = [str(i) + ". " + names[i] for i in range(len(names))]
        subplot.scatter(joints[:, 0], joints[:, 1])

        for i in range(len(joints)):
            parent = parents[i]

            if names[i].startswith("R"):
                subplot.annotate(labels[i], xy=[joints[i, 0], joints[i, 1]],
                                 xytext=[joints[i, 0]-0.3,
                                         joints[i, 1]+0.001])
            else:
                subplot.annotate(labels[i], xy=[joints[i, 0], joints[i, 1]],
                                 xytext=[joints[i, 0]+0.02,
                                         joints[i, 1]+0.001])

            if parent >= 0:
                subplot.plot([joints[i, 0], joints[parent, 0]],
                             [joints[i, 1], joints[parent, 1]])
