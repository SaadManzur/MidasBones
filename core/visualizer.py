import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import core.constants as const


class Visualizer(object):

    def __init__(self):
        super(Visualizer, self).__init__()

        self._jnt_indices = {
            const.HIP: [0, 0],
            const.RHIP: [-0.2, -0.1],
            const.RHIP_KNEE: [-0.2, -0.3],
            const.RKNEE: [-0.2, -0.5],
            const.RKNEE_ANKLE: [-0.2, -0.7],
            const.RANKLE: [-0.2, -0.9],
            const.RANKLE_FOOT: [-0.25, -0.95],
            const.RFOOT: [-0.28, -0.97],
            const.LHIP: [0.2, -0.1],
            const.LHIP_KNEE: [0.2, -0.3],
            const.LKNEE: [0.2, -0.5],
            const.LKNEE_ANKLE: [0.2, -0.7],
            const.LANKLE: [0.2, -0.9],
            const.LANKLE_FOOT: [0.25, -0.95],
            const.LFOOT: [0.28, -0.97],
            const.SPINE1: [0.0, 0.1],
            const.SPINE1_2: [0.0, 0.15],
            const.SPINE2: [0.0, 0.2],
            const.SPINE2_3: [0.0, 0.25],
            const.SPINE3: [0.0, 0.3],
            const.SPINE3_4: [0.0, 0.35],
            const.SPINE4: [0.0, 0.4],
            const.SPINE4_NECK: [0.0, 0.45],
            const.NECK: [0.0, 0.6],
            const.NOSE: [-0.05, 0.65],
            const.HEAD: [0.0, 0.72],
            const.RSHOULDER: [-0.2, 0.5],
            const.RUPPERARM: [-0.25, 0.45],
            const.RSHOULDER_ELBOW: [-0.3, 0.35],
            const.RELBOW: [-0.35, 0.25],
            const.RELBOW_WRIST: [-0.4, 0.15],
            const.RWRIST: [-0.43, 0.1],
            const.RHAND: [-0.45, 0.06],
            const.RHAND_SITE1: [-0.41, 0.02],
            const.RHAND_SITE2: [-0.44, -0.02],
            const.RHAND_SITE3: [-0.48, -0.02],
            const.RHAND_SITE4: [-0.51, 0.02],
            const.LSHOULDER: [0.2, 0.5],
            const.LUPPERARM: [0.25, 0.45],
            const.LSHOULDER_ELBOW: [0.3, 0.35],
            const.LELBOW: [0.35, 0.25],
            const.LELBOW_WRIST: [0.4, 0.15],
            const.LWRIST: [0.43, 0.1],
            const.LHAND: [0.45, 0.06],
            const.LHAND_SITE1: [0.41, 0.02],
            const.LHAND_SITE2: [0.44, -0.02],
            const.LHAND_SITE3: [0.48, -0.02],
            const.LHAND_SITE4: [0.51, 0.02]
        }

    def plot_2d(self, joints=None, parents=None,
                 left=None, right=None, subplot=None):

        if subplot is None:
            fig = plt.figure(figsize=(10, 10))
            subplot = fig.add_subplot(111)
            subplot.set_xlim((-1, 1))
            subplot.set_ylim((-1, 1))

        if joints is None:
            joints = np.vstack(self._jnt_indices.values())

        subplot.scatter(joints[:, 0], joints[:, 1])

        plt.show()
