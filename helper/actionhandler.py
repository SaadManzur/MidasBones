import json

from core.meta import Meta
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
    Visualizer().plot_2d()
