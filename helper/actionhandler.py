import json

from core.meta import Meta
import core.constants as const
from core.visualizer import Visualizer


def dump_meta(filename):
    Meta().dump_sample_meta(filename)


def parse_meta(filename):
    return Meta().parse_meta(filename)


def pick_joints(skeleton, filename):

    with open(filename, 'r') as _file:
        joint_names = json.load(_file)

        return skeleton.pick_joints_by_names(joint_names)


def plot_dummy():
    visualizer = Visualizer()
    visualizer.plot_2d()
    visualizer.show_figure()


def plot_picked_joints(joints, parents, left, right, names):
    visualizer = Visualizer()
    visualizer.plot_2d(joints, parents, names, left, right)
    visualizer.show_figure()
